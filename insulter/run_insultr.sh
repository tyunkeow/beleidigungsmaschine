#!/bin/bash

env

#ping brickd
rm /var/log/insultr.log

python tinkerforge_stack.py
