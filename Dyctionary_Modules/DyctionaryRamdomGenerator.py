#!/usr/bin/env python3
import time
import random

class DyRandomGenerator:
    def __init__(self, ):
        self.Dy_FirstRand = time.time() * random.randint(1, 1000)
        self.Dy_FirstClockPulse = time.clock()
        self.Dy_SecondRand = time.time() * random.randint(1, 1000)
        self.Dy_SecondClockPulse = time.clock()

        self.Dy_RandIncrease = self.Dy_FirstRand * self.Dy_FirstClockPulse * self.Dy_SecondRand * self.Dy_SecondClockPulse
        self.Dy_Divider = random.randint(1, 1000)

        self.Dy_RandResult = (self.Dy_RandIncrease / self.Dy_Divider)

    def DyRandomGet(self, level):
        self.Dy_Final = self.Dy_RandResult % level
        return int(self.Dy_Final)
    