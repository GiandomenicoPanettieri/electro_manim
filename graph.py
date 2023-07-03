from manim import *
from NetList import *
from components import *
from utils import *
from manim_physics import *


class StandingWaveExample(Scene):
    def construct(self):
        wave1 = StandingWave(2,length=1, color = BLUE,amplitude=-0.5,period=5)
        
        #wave2 = StandingWave(2, color = BLUE).shift(RIGHT*2)
        
        waves = Group(wave1)

        self.add(wave1)
        wave1.start_wave()
        self.wait(3)
