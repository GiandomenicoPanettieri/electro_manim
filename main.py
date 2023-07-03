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
        GND1 = GND(" ",0,-3,1)
        
        Q1 = NPNA(" M1 ",-1,0,1)    #NPN1
        Q2 = NPNB("",1,0,1)     #NPN2
        
        A1 = A("I1",0,-2,1)     #tail generator

        R1 = R("R",0.5,1.5,1," ",)
        R2 = R("R",-0.5,1.5,1," ",name_right_shift_offset=-1)
        

        #differential pair input
        in_p = node("Vin+",-1.5,0,color=RED,name_right_shift_offset=-0.5)
        in_n = node("Vin-",1.5,0,color=RED)

        #Supply
        Vdd = Text("Vdd").shift(UP*2.5)

        #source node
        Vs = [0,-0.5,0]
        
        #Net
        net_array =[
            [Q1.ne, Vs, Q2.ne],
            [Vs, A1.n0],
            [Q1.nc, R2.n1],
            [Q2.nc, R1.n1],
            [A1.n1, GND1.n0],
            [[-1.5,2,0], [1.5,2,0]]
        ]    

        Net_List= connect_point_list(net_array)

        self.play(FadeIn(Q1.get_group()),
                  FadeIn(Q2.get_group()),
                  run_time = 1
                  )

        self.play(FadeIn(A1.get_group()), FadeIn(GND1.img), run_time = 0.5)
        self.play(FadeIn(R1.img), FadeIn(R2.img), 
                  FadeIn(Vdd),FadeIn(in_p.get_group()),
                  FadeIn(in_n.get_group()), run_time=0.5)
        self.play(FadeIn(Net_List.img()))

        Circuit = Group(Q1.get_group(),Q2.img)

        self.play(Circuit.animate.shift(LEFT*2))
        self.play(Circuit.animate.rotate(PI))