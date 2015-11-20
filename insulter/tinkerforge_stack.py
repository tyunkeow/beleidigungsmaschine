from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import Master
from tinkerforge.bricklet_motion_detector import MotionDetector
from tinkerforge.bricklet_rotary_poti import RotaryPoti
from tinkerforge.bricklet_io4 import IO4
from text2sound import play_sound
from time import sleep
import sys
from insulter import Insulter
import syslog


class PiTinkerforgeStack:
    #host = '192.168.178.27' #raspi
    #host = '127.0.0.1' #localhost
    host = 'brickd'
    port = 4223
    uid_master = '6JKxCC'
    uid_motion = 'oRL'
    uid_poti_left = 'ejC'
    uid_poti_right = 'ejm'
    uid_io = 'hcs'
    female = False

    def __init__(self):
        syslog.openlog('insultr-tf', 0, syslog.LOG_LOCAL4)
        self.con = IPConnection()
        self.master = Master(self.uid_master, self.con)
        self.motion = MotionDetector(self.uid_motion, self.con)
        self.poti_left = RotaryPoti(self.uid_poti_left, self.con)
        self.poti_right = RotaryPoti(self.uid_poti_right, self.con)
        self.io = IO4(self.uid_io, self.con)
        self.insulter = Insulter()
        self.log("---" + str(15^15))
        self.log("---" + str(15^14))

    def log(self, msg):
        syslog.syslog(msg)

    def connect(self):
        self.log("Connecting to host " + self.host + " on port " + str(self.port))
        self.con.connect(self.host, self.port)
        self.set_ziel_geschlecht(self.io.get_value())

    def disconnect(self):
        self.log("Disconnecting from host " + self.host)
        self.con.disconnect()

    def motion_detected(self):
        self.log("CALLBACK!!")
        self.insult()

    def insult(self):
        ziel_geschlecht = "m"
        if self.female:
            ziel_geschlecht = "f"
        self.insulter.speak_next_insult(ziel_geschlecht, self.poti_left.get_position(), self.poti_right.get_position())

    def motion_cycle_ended(self):
        self.log("READY for motion detection!")

    def io_switch(self, interrupt_mask, value_mask):
        self.log("IO4 triggered")
        self.log('Interrupt by: ' + str(bin(interrupt_mask)))
        self.log('Value: ' + str(bin(value_mask)))
        #print('Val1: ' + str(value_mask))

        if interrupt_mask == 1:
            self.log("Sex switched...")
            # button 1 switched
            self.set_ziel_geschlecht(value_mask)
        elif interrupt_mask == 2:
            self.log("Insult button pressed...")
            button_up = value_mask&2
            self.log("value_mask =" + str(button_up))
            if button_up == 2:
                self.insult()
        self.log("io_switch() end")

    def set_ziel_geschlecht(self, value_mask):
        is_on = value_mask^14
        if is_on:
            self.log("sex was set to MALE")
            self.female = False
        else:
            self.log("sex was set to FEMALE")
            self.female = True


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
    #print "Distance Infrared 1         : {} cm".format(stack.distance_ir_1.get_distance()/10)
    #print "MultiTouch electrode config : ", stack.multi_touch_1.get_electrode_config()
    print "Poti left position  : ", stack.poti_left.get_position()
    print "Poti right position : ", stack.poti_right.get_position()
    stack.register_callbacks()
    stack.insulter.say_hello()

    sleep(1000000)
    input('Press key to exit\n')
    stack.disconnect()


