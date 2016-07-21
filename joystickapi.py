# -*- coding: utf-8 -*-
"""
Joystickapi
author: Ninfeion
"""
import pygame.joystick
import threading,time

class devController(object):
    def __init__(self):
        #pygame.joystick.init()
        self.devNum = None

        self.name = None
        self.id = None
        self.axesNum = None
        self.ballsNum = None
        self.buttonsNum = None
        self.hatsNum = None

        self._axis = []
        self._ball = []
        self._hat = []
        self._button = []

        self._joystickLoop = False

    def controllerScan(self):
        pygame.init()
        pygame.joystick.init()

        self.devNum = pygame.joystick.get_count()
        return self.devNum

    def getControllerName(self, devNum):
        pass

    def controllerChoose(self, joystickNum):
        self._instancejoystick = pygame.joystick.Joystick(joystickNum)
        self._instancejoystick.init()

        self.name = self._instancejoystick.get_name()
        self.id = self._instancejoystick.get_id()
        self.axesNum = self._instancejoystick.get_numaxes()
        self.ballsNum = self._instancejoystick.get_numballs()
        self.buttonsNum = self._instancejoystick.get_numbuttons()
        self.hatsNum = self._instancejoystick.get_numhats()

    def _eventRefresh(self):
        pygame.event.get()

    def controllLoopEvent(self, refreshtime):
        while self._joystickLoop == True:
            time.sleep(refreshtime)
            self.controllerDataRefresh()

    def controllThreading(self, openorno, refreshtime):
        if openorno == True:
            self._joystickLoop = True
            self._jThreading = threading.Thread(target=self.controllLoopEvent, args=(refreshtime,))
            self._jThreading.setDaemon(True)
            self._jThreading.start()
        elif openorno == False:
            self._joystickLoop = False
            self._jThreading.join()

    def controllerDataRefresh(self):
        self._eventRefresh()

        if self._axis:
            for i in range(self.axesNum):
                self._axis[i] = self._instancejoystick.get_axis(i)
        else:
            for i in range(self.axesNum):
                self._axis.append(self._instancejoystick.get_axis(i))

        if self._button:
            for i in range(self.buttonsNum):
                self._button[i] = self._instancejoystick.get_button(i)
        else:
            for i in range(self.buttonsNum):
                self._button.append(self._instancejoystick.get_button(i))

        if self._ball:
            for i in range(self.ballsNum):
                self._ball[i] = self._instancejoystick.get_ball(i)
        else:
            for i in range(self.ballsNum):
                self._ball.append(self._instancejoystick.get_ball(i))

        if self._hat:
            for i in range(self.hatsNum):
                self._hat[i] = self._instancejoystick.get_hat(i)
        else:
            for i in range(self.hatsNum):
                self._hat.append(self._instancejoystick.get_hat(i))

        #return self._axis,self._button,self._hat,self._ball #return a tuple which including list

    def getData(self):
        return self._axis, self._button, self._hat, self._ball