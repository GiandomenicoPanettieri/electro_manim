from manim import *
from NetList import *
from components import *
from utils import *


class Myscene(Scene): 

    def construct(self):

        #optional plane to get a cartesian system of coordinates
        #plane = NumberPlane()
        #self.add(plane)

        

        #create an object from R class
        GND1 = GND(" ",0,-3,1)
        
        Q1 = NPNA("",-1,0,1)    #NPN1
        Q2 = NPNB("",1,0,1)     #NPN2
        
        A1 = A("I1",0,-2,1)     #tail generator

        R1 = R("R",0.5,1.5,1," ",)
        R2 = R("R",-0.5,1.5,1," ",name_right_shift_offset=-1)
        self.add(R1.get_group(),R2.get_group())

        #differential pair input
        in_p = node("Vin+",-1.5,0,color=RED,name_right_shift_offset=-1.5)
        in_n = node("Vin-",1.5,0,color=RED)

        #source node
        Vs = [0,-0.5,0]


        

        Net_List = Net()

        Net1 = [

            Q1.ne,
            Vs,
            Q2.ne

        ]

        Net_List = Net(connect_nodes_oriented(Net1))

        Net1 = [
            Vs,
            A1.n0
        ]

        Net_List.merge_subnet(Net(connect_nodes_oriented(Net1)))

        Net1 = [
            Q1.nc,
            R2.n1
        ]

        Net_List.merge_subnet(Net(connect_nodes_oriented(Net1)))

        Net1 = [
            Q2.nc,
            R1.n1
        ]

        Net_List.merge_subnet(Net(connect_nodes_oriented(Net1)))
        
        self.add(Net_List.img())

        self.play(FadeIn(Q1.get_group()),
                  FadeIn(Q2.get_group()),
                  FadeIn(A1.img),
                  FadeIn(R1.get_group()),
                  FadeIn(R2.get_group()),
                  FadeIn(GND1.img),
                  FadeIn(in_p.get_group()),
                  FadeIn(in_n.get_group())
                  )


       