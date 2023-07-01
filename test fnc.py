from manim import *
from ELECTRONIC_MANIM import *

#

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        P1 = node( "A" , 0,0)
        P2 = node( "B" , 1,1)
        P3 = node( "C" , 2,1)
        P4 = node( "D" , 1,0)
        P5 = node( "E" , 0,3)
        P6 = node( "F" , 1,4)
        P7 = node( "G" , 2,2)
        P8 = node( "H" , 1,6)
        self.add(P1.get_group())
        self.add(P2.get_group())
        self.add(P3.get_group())
        self.add(P4.get_group())
        self.add(P5.get_group())
        self.add(P6.get_group())
        self.add(P7.get_group())
        self.add(P8.get_group())
        

        node_list = [
            P1.n0,
            P2.n0,
            P3.n0,
            P4.n0,
            P5.n0,
            P6.n0,
            P7.n0,
            P8.n0
        ]

        pippo= connect_nodes_oriented(node_list)
        for i in range(0,len(pippo)):
            self.add(pippo[i])
        