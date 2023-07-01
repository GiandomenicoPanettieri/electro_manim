from manim import *
from ELECTRONIC_MANIM import *

#this code creates a parllel RLC resonator

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        #plane = NumberPlane()
        #self.add(plane)

        R1 = R(name="R1", x0=-3,
               y0=1, size=2,value_text="3k",value_font_scale=0.7,
               value_up_shift_offset=0)
        R1_img=R1.get_group()
'''        L1 = L(name="R1",value_text="17.4n",x0=3,y0=1,
               size=2,value_font_scale=0.8,value_right_shift_offset=0.4)
        L1_img = L1.get_group()

        C1 = C("C1",0,1,2,"100p",1,0.6, name_up_shift_offset=0)
        C1_img = C1.get_group()

        R1L1C1=Group(R1_img,L1_img,C1_img)
        self.play(FadeIn(R1L1C1))
        self.wait(3)'''



        
        
        
        

        
