from manim import *
from NetList import *
from components import *
from utils import *
from manim_physics import*


class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        #plane = NumberPlane()
        #self.add(plane)
				

        #ground
        GND1 = GND(" ",0,-3.5,1)
        #MOS
        M1 = NMOSA("M1",1,-1,1)      #NPN1
        M2 = NMOSB("M2",-1,-1,1)     #NPN2
        #tail generator
        A1 = A("I1",0,-2.5,1)
        #Supply
        Vdd = Text("Vdd").shift(UP*3.5)
        Vdd = Vdd.scale(0.6)


				#resonator
        R1 = R("R1", 0,0.5,1)     #resistor
        R1.rotate_component(PI/2)

        C1 = C("C1", 0,1.5,1)     #capacitor
        C1.rotate_component(PI/2)

        L1 = L("L1", -1,2.5,1)
        L1.rotate_component(PI/2)
        L2 = L("L1", 1,2.5,1)     #two inductors that will be in series
        L2.rotate_component(PI/2)
    
        resonator = Group (R1.img,C1.img,L1.img,L2.img)

				#output waves
        Voutp_w = StandingWave(2,length = 1, color = BLUE, amplitude = 0.5).shift(LEFT*2.5+UP)
        Voutn_w = StandingWave(2,length = 1, color = BLUE, amplitude = -0.5).shift(RIGHT*2.5+UP)
				
				#Netlist
        net_array = [           #specifiesall the points that will be connected 
            [L1.n1,L2.n0],
            [C1.n0,[-1.5,1.5,0]],
            [C1.n1,[1.5,1.5,0]],
            [R1.n0,[-1.5,0.5,0]],
            [R1.n1,[1.5,0.5,0]],
            [L1.n0,[-1.5,0.5,0]],
            [L2.n1,[1.5,0.5,0]]
        ]
        Net_List_resonator=connect_point_list(net_array) #generates the resonator's netlist
				
        net_array = [
            [M1.ng, [-1.5,0,0], L1.n0],
            [M2.ng, [1.5,0,0], L2.n1],
            [M2.nd,[-1.5,0,0]],
            [M1.nd,[1.5,0,0]],
            [M1.ns,M2.ns],
            [[0,-1.5,0],A1.n0],     #Tail
            [A1.n1,GND1.n0],        #Tail
            [[0,2.5,0],[0,3,0]],    #supply
            [[-2,3,0], [2,3,0]],
            [[1.5,1.5,0],[2,1.5,0]], #output
            [[-1.5,1.5,0],[-2,1.5,0]]
        ]
        sub_net1 = connect_point_list(net_array) #remaining net_list
        Net_List = Net_List_resonator
        
        
        Voutp = node(" ",2,1.5)
        Voutn = node(" ",-2,1.5)

        #Animations
        #resonator
        self.play(GrowFromPoint(R1.img,ORIGIN),
                  GrowFromPoint(C1.img,[0,2,0]),
                  GrowFromPoint(L1.img,[-1,3,0]),
                  GrowFromPoint(L2.img,[1,3,0]))    
        
        self.play(FadeIn(Net_List_resonator.img()))
        self.wait(0.5)
        self.play(Circumscribe(resonator))

        #oscillator
        self.play(GrowFromEdge(M1.img,LEFT),run_time = 0.5)
        self.play(GrowFromEdge(M2.img,RIGHT),run_time = 0.5)
        self.play(Indicate(M1.img),Indicate(M2.img),FadeIn(A1.img),FadeIn(GND1.img))
        self.play(FadeIn(sub_net1.img()),FadeIn(Voutp.img),FadeIn(Voutn.img))

        #text and waves
        Vp = Text("V+",color = BLUE).shift(UP*1.8+RIGHT*2.5)   
        Vp = Vp.scale(0.6)
        Vn = Text("V-",color = BLUE).shift(UP*1.8+RIGHT*(-2.5))   
        Vn = Vn.scale(0.6)
        self.play(FadeIn(Voutp_w),FadeIn(Voutn_w),
                  Write(Vp),Write(Vn),Write(Vdd)
                  )
        Voutn_w.start_wave()
        Voutp_w.start_wave()
        self.wait(3)
        Voutn_w.stop_wave()
        Voutp_w.stop_wave()

        Net_List.merge_subnet(sub_net1)         #connection of the netlists into a single NetList
        My_Oscillator = Group(M1.img,M2.img,Voutp.img,Voutn.img,Vdd,
                              A1.img,GND1.img, Voutp_w, Voutn_w, Vn,Vp,
                              resonator, Net_List.img())
        
        
        self.play(My_Oscillator.animate.shift(RIGHT*2))
        self.play(My_Oscillator.animate.scale(0.7))

        self.wait(3)

				


        

        
