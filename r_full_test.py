from manim import *
from NetList import *
from components import *
from utils import *


class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        Rd = R( name = "Rd", value_text="3k",
                x0=0,y0=2, size=1)
        Rd_img = Rd.get_group()

        
        Rs = R( name = "Rs", value_text="2k",
                x0=0,y0=-1.5, size=1)
        Rs_img = Rs.get_group()

        Cs = C( name = "Cs", value_text = "1n",
                x0=1,y0=-1.5, size= 1
               )
        Cs_img = Cs.get_group()

        M1 = NMOS(name = "M1", x0=-0.5 , y0=0, size=1)
        M1_img = M1.get_group()

        Rs = R( name = "Rs", value_text="3k",
                x0=0,y0=2, size=1)
        Rs_img = Rs.get_group()

        GND1 = GND(" ",0,-3,1)
        GND1_img = GND1.get_group()

        self.play(M1_img.invert)

        self.wait(2)

        
        





        
          

        