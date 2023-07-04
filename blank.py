from manim import *
from NetList import *
from components import *
from utils import *
from manim_physics import*


class Myscene(Scene): 
    def play_obj(self, to_play):
            self.play(*to_play)
    def add_obj(self,to_play):
            self.add(*to_play)

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        self.wait(2)
        