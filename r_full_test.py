from manim import *
from ELECTRONIC_MANIM import *

#this code creates a parllel RLC resonator

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        R1=R("R1",0,0,1,"1k")
        R1_img=R1.get_group()
        '''R = ImageMobject("texture\R").scale(0.18)
        R = R.shift(RIGHT*0.014)
        n1 = [0, 0.5]0
        n2 = [0, -0.5]'''

        R1_img.shift(1*RIGHT+1*UP)
        self.add(R1_img)
        self.play(
            Rotate(
                R1_img,
                angle=12*PI,
                rate_func=linear,
                about_point =(0,0,0),
                run_time=6)
        )