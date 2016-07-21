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

        #self.controllList = {'Yaw': 0,'Pitch': 1,'Roll': 2,'Thrust': 3, 'Damping':4}

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




        