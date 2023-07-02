from manim import *
from NetList import *
from components import *
from utils import *


class Myscene(Scene): 

    def construct(self):

        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        net_array = [
            [[0,0,0],[1,1,0]]
        ]

        Net_List = connect_point_list(net_array)
        self.add(Net_List.img()) #to add the image 

       