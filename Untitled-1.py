from manim import *
from NetList import *
from components import *
from utils import *
from manim_physics import*


class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        net_point = [
            [[-1,-1,0],[-1,1,0],[1,0,0],[-1,-1,0]],
            [[-1,0.75,0],[-1.5,0.75,0]]
        ]
        NetList = connect_point_list(net_point, BLUE)
        #NetList.color_list(color=GREEN)
        self.add(NetList.img())

        a = Line([0,0,0],[1,1,0], color = BLUE)
        #a.color(BLUE)
        self.add(a)
        print(NetList.points)
        NetList = connect_point_list(NetList.points, GREEN)
        self.add(NetList.img())