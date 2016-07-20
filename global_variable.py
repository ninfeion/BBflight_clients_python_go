# -*- coding: utf-8 -*-

"""
global variable bank
author: Ninfeion
"""

import serial,bbapi
import joystickapi

BBSerial = serial.Serial()
BBSerialRecieve = bbapi.serial_recieve()
BBSerialSend = bbapi.serial_send()
BBController = joystickapi.devController()

