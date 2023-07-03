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

        #create an object from R class
        GND1 = GND(" ",0,-2.5,1)
        
        M1 = NMOSA("M1",1,0,1)    #NPN1
        M2 = NMOSB("M2",-1,0,1)     #NPN2
        
        A1 = A("I1",0,-1.5,1)     #tail generator

        self.add(M1.img, M2.img, A1.img,GND1.img)
        
        #resonator
        R1 = R("R1", 0,2,2, " ")
        R1.rotate_img(PI/4, [0,2,0])
        self.add(R1.img)

        

        #Supply
        Vdd = Text("Vdd").shift(UP*2.5)


        #output waves
        Voutp_w = StandingWave(2,length = 1, color = BLUE, amplitude = 0.5).shift(LEFT*2.5+UP)
        
        Voutn_w = StandingWave(2,length = 1, color = BLUE, amplitude = -0.5).shift(RIGHT*2.5+UP)
        


        #animations
        self.add(Voutp_w,Voutn_w)
        Voutn_w.start_wave()
        Voutp_w.start_wave()
        self.wait(3)
        
        