from manim import *
from ELECTRONIC_MANIM import *

#

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        M1 = NMOS(name="M1",x0=0.5,y0=0.5, size = 1)
        M1_img = M1.get_group()
        self.add(M1_img)
