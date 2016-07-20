# -*- coding: utf-8 -*-
"""
Joystickapi
author: Ninfeion
"""
import pygame.joystick

class devController(object):
    def __init__(self):
        pygame.joystick.init()

        self.devNum = None

        self.name = None
        self.id = None
        self.axesNum = None
        self.ballsNum = None
        self.buttonsNum = None
        self.hatsNum = None

    def controllerScan(self):
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

    def controllLoopEvent(self):
        pass

    def controllThreading(self, openorno):
        pass














    def getControllerData(self):
        self._axis = []
        self._ball = []
        self._hat = []
        self._button = []

        self._eventRefresh()
        for i in range(self.axesNum):
            self._axis.append(float("%1.3f" % self._instancejoystick.get_axis(i)))
            #print("Axis %i value: %f \n" % (i, self._axis[-1]))
        for i in range(self.buttonsNum):
            self._button.append(self._instancejoystick.get_button(i))
            #print("Button %i value: %s \n" % (i, self._button[-1]))
        for i in range(self.ballsNum):
            self._ball.append(self._instancejoystick.get_ball(i))
            #print("Ball %i value: %s \n" % (i, str(self._ball[-1])))
        for i in range(self.hatsNum):
            self._hat.append(self._instancejoystick.get_hat(i))
            #print("Hat %i value: %s \n" % (i, str(self._hat[-1])))

        return self._axis,self._button,self._hat,self._ball #return a tuple which including list