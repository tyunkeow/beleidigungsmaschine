from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import Master
from tinkerforge.bricklet_motion_detector import MotionDetector
from tinkerforge.bricklet_rotary_poti import RotaryPoti
from tinkerforge.bricklet_io4 import IO4
from time import sleep
import os
import sys
from insultr import Insultr
import syslog


class PiTinkerforgeStack:
    #host = '192.168.178.36' #raspi
    #host = '127.0.0.1' #localhost
    host = 'brickd'
    port = 4223
    female = False
    io = None
    poti_left = None
    poti_volume = None
    master = None

    def __init__(self):
        syslog.openlog('insultr-tf', 0, syslog.LOG_LOCAL4)

        self.con = IPConnection()

        # Register IP Connection callbacks
        self.con.register_callback(IPConnection.CALLBACK_ENUMERATE, 
                                     self.cb_enumerate)
        self.con.register_callback(IPConnection.CALLBACK_CONNECTED, 
                                     self.cb_connected)
        
        self.insultr = Insultr()
        self.set_volume(50)
        self.log("---" + str(15^15))
        self.log("---" + str(15^14))

    def log(self, msg):
        syslog.syslog(msg)
        print msg

    def connect(self):
        self.log("Connecting to host " + self.host + " on port " + str(self.port))
        self.con.connect(self.host, self.port)
        self.con.enumerate()

    def disconnect(self):
        self.log("Disconnecting from host " + self.host)
        self.con.disconnect()

    # Callback handles device connections and configures possibly lost 
    # configuration of lcd and temperature callbacks, backlight etc.
    def cb_enumerate(self, uid, connected_uid, position, hardware_version, 
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
            
            self.log("cb_enumerate() id {} - Found device: ident={}, position={}".format(uid, device_identifier, position))
            if device_identifier == IO4.DEVICE_IDENTIFIER:
                self.log("cb_enumerate() id {} - Creating IO4 device object".format(uid))
                self.io = IO4(uid, self.con) 
                self.io.set_debounce_period(1000)

                if position == 'a':
                    self.log("cb_enumerate() id {} - Configuring IO4 device object at position a (switches).".format(uid))
                    self.io.register_callback(self.io.CALLBACK_INTERRUPT, self.io_switch)
                    self.io.set_configuration(15, 'i', True)
                    # Enable interrupt on pin 0 and 1
                    self.io.set_interrupt(1 << 0)
                    self.io.set_interrupt(1 << 1)
                    self.set_ziel_geschlecht(self.io.get_value())
                else:
                    self.log("cb_enumerate() id {} - Configuring IO4 device object at position ? (lights, shutdown).".format(uid))
                    self.io.set_configuration((1 << 0) | (1 << 1), "o", True)

            elif device_identifier == RotaryPoti.DEVICE_IDENTIFIER:
                self.log("cb_enumerate() id {} - Creating RotaryPoti device object".format(uid))
                self.poti_volume = RotaryPoti(uid, self.con) 
                self.poti_volume.set_position_callback_period(100)
                self.poti_volume.register_callback(self.poti_volume.CALLBACK_POSITION, self.poti_volume_changed)
            elif device_identifier == Master.DEVICE_IDENTIFIER:
                self.log("cb_enumerate() id {} - Creating Master device object".format(uid))
                self.master = Master(uid, self.con)
            else: 
                self.log("cb_enumerate() id {} - Could not register unknown device bricklet".format(uid))

    # Callback handles reconnection of IP Connection
    def cb_connected(self, connected_reason):
        # Enumerate devices again. If we reconnected, the Bricks/Bricklets
        # may have been offline and the configuration may be lost.
        # In this case we don't care for the reason of the connection
        self.con.enumerate()    

    def motion_detected(self):
        self.log("CALLBACK!!")
        self.insult()

    def insult(self):
        self.insultr.speak_next_insult()

    def set_volume(self, volume_percent=50):
        set_volume_cmd = 'amixer sset Master {}%'.format(volume_percent)
        self.log("set_volume() Setting volume with command: " + set_volume_cmd)
        os.system(set_volume_cmd)

    def set_volume_from_poti(self):
        if self.poti_volume:
            position = self.poti_volume.get_position()
            self.poti_volume_changed(position)
        else:            
            self.set_volume(50)

    def poti_volume_changed(self, position=0):
        self.log("poti_volume_changed() poti was set to position {}".format(position))
        if position > 150:
            position = 150
        if position < -150:
            position = -150
        MIN_VOLUME = 25.0
        MAX_VOLUME = 90.0
        poti_percent = ((position + 150.0) / 300.0) # between 0.0 and 1.0
        volume_percent = MIN_VOLUME + ((MAX_VOLUME-MIN_VOLUME)*poti_percent)
        self.set_volume(volume_percent)

    def motion_cycle_ended(self):
        self.log("READY for motion detection!")

    def io_switch(self, interrupt_mask, value_mask):
        self.log("io_switch() IO4 triggered")
        self.log("io_switch() Interrupt by {} / {} ".format(str(bin(interrupt_mask)), interrupt_mask))
        self.log('io_switch() Value: ' + str(bin(value_mask)))
        
        self.set_volume_from_poti()

        if interrupt_mask == 1:
            self.log("io_switch() Sex switched...")
            # button 1 switched
            self.set_ziel_geschlecht(value_mask)
        elif interrupt_mask == 2:
            self.log("io_switch() Insult button pressed...")
            button_up = value_mask&2
            self.log("io_switch() value_mask =" + str(button_up))
            if button_up == 2:
                self.insult()
        else: 
            self.log("io_switch() Don't know what to do with interrupt_mask {}".format(interrupt_mask))
        self.log("io_switch() end")

    def set_ziel_geschlecht(self, value_mask):
        is_on = value_mask^14
        if is_on:
            self.log("sex was set to MALE")
            self.female = False
            self.insultr.set_maennlich()
            self.io.set_configuration(1 << 0, "o", True)
            self.io.set_configuration(1 << 1, "o", False)
        else:
            self.log("sex was set to FEMALE")
            self.female = True
            self.insultr.set_weiblich()
            self.io.set_configuration(1 << 0, "o", False)
            self.io.set_configuration(1 << 1, "o", True)


    def register_callbacks(self):
        self.log("Registering callback to motion detector...")
        self.motion.register_callback(self.motion.CALLBACK_MOTION_DETECTED, self.motion_detected)
        self.motion.register_callback(self.motion.CALLBACK_DETECTION_CYCLE_ENDED, self.motion_cycle_ended)
        self.io.set_debounce_period(1000)
        self.io.register_callback(self.io.CALLBACK_INTERRUPT, self.io_switch)
        # Enable interrupt on pin 0
        self.io.set_interrupt((1 << 0) | (1 << 1))
        #self.io.set_interrupt(1 << 1)
        self.log("register done")


if __name__ == "__main__":
    stack = PiTinkerforgeStack()
    stack.connect()
    if stack.poti_left:
        print "Poti left position  : ", stack.poti_left.get_position()
    if stack.poti_volume:
        print "Poti volume position : ", stack.poti_volume.get_position()
    #stack.register_callbacks()
    stack.insultr.say_hello()

    sleep(1000000)
    input('Press key to exit\n')
    stack.disconnect()


