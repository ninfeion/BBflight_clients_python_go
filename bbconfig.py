# -*- coding: utf-8 -*-
"""
BB config
author: Ninfeion
"""

class clientConfig(object):
    def __init__(self):
        self._yawMapping = [0, 'Yaw']
        self._pitchMapping = [1, 'Pitch']
        self._rollMapping = [4, 'Roll']
        self._thrustMapping = [2, 'Thrust']
        self._dampingMapping = [3, 'Damping']
        self.controllList = ['Thrust', 'Pitch', 'Roll', 'Yaw', 'Damping']
        self._slaveAddress= [0x34, 0xc3, 0x10, 0x10, 0x11]

        self._flightMode = ''
        self._thrustMode = ''

        self._rollTrim = 0.00
        self._pitchTrim = 0.00

        self._maxAngle = 0
        self._maxYawAngle = 0
        self._maxThrust = 0.00 #unit:%
        self._minThrust = 0.00
        self._slewLimit = 0.00
        self._thrustLoweringSlewrate = 0.00

        self._controllerConnectStatus = None
        self._serialConnectStatus = None

        self._slaveConnectStatus = None

        self._connectRespond = False

        self.slaveRoll = 0
        self.slavePitch = 0
        self.slaveYaw = 0
        self.slaveThrust = 0
        self.slaveM1 = 0
        self.slaveM2 = 0
        self.slaveM3 = 0
        self.slaveM4 = 0
        self.slaveBattery = 0
        self.slaveLinkQuality = 0


    def builtConnectWithSlave(self):
        """Return 32 bytes"""
        return bytes([0xaa, 0xaa,
                      self._slaveAddress[0], self._slaveAddress[1],
                      self._slaveAddress[2], self._slaveAddress[3], self._slaveAddress[4],
                      0x01,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                      0xff, 0xff])

    def createControllData(self, datagroup):
        """datagroup = [thrustValue, pitchAngle, rollAngle, yawAngle, dampingValue]"""
        return bytes([0xaa, 0xaa,
                      self._slaveAddress[0], self._slaveAddress[1],
                      self._slaveAddress[2], self._slaveAddress[3], self._slaveAddress[4],
                      0x01,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00,
                      0x00, 0x00,
                      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                      0xff, 0xff])

    def respondAnalysis(self, string):
        #import binascii
        if len(string) == 64:
            mssgroup = []
            for i in range(32):
                mssgroup.append(int(string[:2],base= 16))
                string = string[2:]
            if mssgroup[0]==0xaa and mssgroup[1]==0xaa and mssgroup[30]==0xff and mssgroup[31]==0xff:
                self._connectRespond = mssgroup[7]

                self.slaveRoll = int(chr(mssgroup[8]) + chr(mssgroup[9]) + chr(mssgroup[10]) + chr(mssgroup[11]))/10 - 180
                self.slavePitch = int(chr(mssgroup[12]) + chr(mssgroup[13]) + chr(mssgroup[14]) + chr(mssgroup[15]))/10 - 180
                self.slaveYaw = int(chr(mssgroup[16]) + chr(mssgroup[17]) + chr(mssgroup[18]) + chr(mssgroup[19]))/10 - 180
                self.slaveThrust = mssgroup[21]*256 + mssgroup[20]
                self.slaveM1 = mssgroup[22]
                self.slaveM2 = mssgroup[23]
                self.slaveM3 = mssgroup[24]
                self.slaveM4 = mssgroup[25]
                self.slaveBattery = mssgroup[26]
                self.slaveLinkQuality = mssgroup[27]

            else:
                return 'Command Error'

    def setControllerConnectStatus(self, par):
        self._controllerConnectStatus = par

    def setSerialConnectStatus(self, par):
        self._serialConnectStatus = par

    def checkIfReadyForSlaveConnect(self):
        if self._controllerConnectStatus == True and self._serialConnectStatus == True:
            return True
        else:
            return False

    def isConnectSlave(self):
        return self._connectRespond

    def slaveUnconnect(self):
        self._connectRespond = False

    def controllerRawDataConvertAttitude(self, rawData):
        yawAngle = rawData[0][self._yawMapping[0]] * 180
        pitchAngle = rawData[0][self._pitchMapping[0]] * 180
        rollAngle = rawData[0][self._rollMapping[0]] * 180

        thrustValue = rawData[0][self._thrustMapping[0]]* 1000 + 1000
        dampingValue = rawData[0][self._dampingMapping[0]]* 1000 + 1000

        return thrustValue, pitchAngle, rollAngle, yawAngle, dampingValue

    def setYawMapping(self, axisNum):
        self._yawMapping[0] = axisNum

    def setPitchMapping(self, axisNum):
        self._pitchMapping[0] = axisNum

    def setRollMapping(self, axisNum):
        self._rollMapping[0] = axisNum

    def setThrustMapping(self, axisNum):
        self._thrustMapping[0] = axisNum

    def setDampingMapping(self, axisNum):
        self._dampingMapping[0] = axisNum

    def forControllerNumFindMapping(self, axisNumOrOther):
        for i in [self._yawMapping, self._thrustMapping, self._rollMapping, self._pitchMapping, self._dampingMapping]:
            if i[0] == axisNumOrOther:
                nametemp = i[1]
            else:
                continue
        for i in range(len(self.controllList)):
            if self.controllList[i] == nametemp:
                return i
            else:
                continue

    def getSlaveAddress(self):
        return '0x%02x,0x%02x,0x%02x,0x%02x,0x%02x' % (self._slaveAddress[0],self._slaveAddress[1],
                                                       self._slaveAddress[2],self._slaveAddress[3],
                                                       self._slaveAddress[4])

    def setSlaveAddress(self, address):
        """accept the parameter like string'0xaa,0xaa,0xaa,0xaa,0xaa'"""
        import re
        addressafter = re.findall(r'[0][x][0-9a-fA-F]{2,2}', address)
        for i in range(len(self._slaveAddress)):
            self._slaveAddress[i] = eval(addressafter[i])
        