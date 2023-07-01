from manim import *
from ELECTRONIC_MANIM import *

#this code creates a parllel RLC resonator

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        #plane = NumberPlane()
        #self.add(plane)

        #form ELECTRONIC_MANIM
        res1=animated_circuit.animated_resonator(self ,"L2","C2","R2","1n","1p","1k")
        
        self.play(res1.animate.shift(UP*2+LEFT*0.05))
        self.play(res1.animate.scale(0.8))

        #component and placements
        Q1 = ImageMobject("texture\\nmos").scale(0.18)
        Q1 = Q1.shift(0.448*LEFT) #MOS placing
        E1 = ImageMobject("texture\\Vin").scale(0.25)
        E1 = E1.shift(2.181*LEFT+1*DOWN)
        GND1 = ImageMobject("texture\gnd").scale(0.1)
        GND1 = GND1.shift(2.3*DOWN+RIGHT*0.03)#GND placing
        GND2 = ImageMobject("texture\gnd").scale(0.1)
        GND2 = GND2.shift(2.3*DOWN+RIGHT*0.03+2*LEFT)#GND placing



        #net trace
        line_GND1_Q1s = Line((0,-2,0),(0,-0.5,0))
        line_res1_Q1d = Line((0,0.5,0),(0,1.3,0))
        line_Q1g_Vin_1 = Line((-1,0,0),(-2,0,0))
        line_Q1g_Vin_2 = Line( (-2,0,0),(-2,-0.7,0))
        line_Vin_GND2  = Line((-2,-1.4,0),(-2,-2,0))

        #texts
        textQ1 = Text("M1",
                       font_size=30)
        textQ1 = textQ1.shift(0.7*RIGHT)

        Vdd = Text("Vdd",
                   font_size=30)
        Vdd = Vdd.shift(3*UP)


        #animations
        
        self.play(FadeIn(Vdd),run_time=0.3)
        self.play(FadeIn(Q1),run_time=0.3)
        self.play(Write(textQ1), run_time=0.3)
        self.play(FadeIn(GND1),run_time=0.3)
        self.play(FadeIn(GND2),run_time=0.3)
        self.play(FadeIn(E1),run_time = 0.3)
        self.play(Write(line_res1_Q1d), run_time=0.2)
        self.play(Write(line_GND1_Q1s), run_time=0.2)
        self.play(Write(line_Q1g_Vin_1), run_time=0.2)
        self.play(Write(line_Q1g_Vin_2), run_time=0.2)
        self.play(Write(line_Vin_GND2), run_time=0.2)
        
        circuit1 = Group(res1,Vdd,Q1,textQ1,GND1,GND2,E1,
                         line_res1_Q1d,line_GND1_Q1s,line_Q1g_Vin_1,
                         line_Q1g_Vin_2, line_Vin_GND2)
        self.play(circuit1.animate.shift(2*LEFT))



        '''line_GND1_Q1s_P1 = (0,0,0)
        line_GND1_Q1s_P2 = (1,0,0)
        line_GND1_Q1s = Line(line_GND1_Q1s_P1,line_GND1_Q1s_P2)
        dotc = Dot(color=GREEN).shift(line_GND1_Q1s.get_center())
        dotc = dotc.shift(LEFT*(line_GND1_Q1s_P1[0]+line_GND1_Q1s_P2[0])/2)
        self.play(Write(line_GND1_Q1s), run_time=0.2)
        self.add(dotc)
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))
        self.play(dotc.animate.shift(RIGHT*line_GND1_Q1s_P2[0]), run_time=0.5)
        self.add(dotc.shift(RIGHT*(-line_GND1_Q1s_P2[0])))'''

        
        

        
            

        
        
        
        

        
        
        
        
        