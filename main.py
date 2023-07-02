from manim import *
from NetList import *
from components import *
from utils import *


class Myscene(Scene): 

    def construct(self):

        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        #create an object from R class

        MOS1 = NMOSB("M1",-2,2,2)
        self.add(MOS1.get_group())

        MOS2 = NMOSA("M2",2,0,2)
        self.add(MOS2.get_group())

        
        self.wait(1)






        
        





        
          

        