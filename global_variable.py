# -*- coding: utf-8 -*-

"""
global variable bank
author: Ninfeion
"""

import serial,bbapi

BBSerial = serial.Serial()
BBSerialRecieve = bbapi.serial_recieve()
BBSerialSend = bbapi.serial_send()

