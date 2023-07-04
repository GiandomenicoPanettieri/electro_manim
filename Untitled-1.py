from manim import *
from NetList import *
from components import *
from utils import *
from manim_physics import*


class Myscene(Scene): 
    def play_obj(self, to_play):
            self.play(*to_play)
    def add_obj(self,to_play):
            self.add(*to_play)

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)


        opa1 = opamp(x0=0,y0=0,name="op1",color=BLUE,color_name = GREEN)
        R1 = R(name=" ",x0=0,y0=1,size = 1)    

        self.play_obj(opa1.circuit)

        print(opa1.nplus)
        print(opa1.nminus)
        print(opa1.nout)

        opa1.rotate_component(PI)
        print(opa1.nplus)
        print(opa1.nminus)
        print(opa1.nout)        

        '''size = 1
        x0 = 0
        y0= 0
        name = "op1"
        color_name = GREEN
        name_right_shift_offset = -0.25
        name_up_shift_offset = 0
        name_font_scale = 0.7
        plus = Text("+").shift(RIGHT*(-0.8+x0)+UP*(0.6+y0))
        plus.scale(0.7*size)
        minus= Text("-").shift(RIGHT*(-0.8+x0)+UP*(-0.6+y0))
        minus.scale(0.7*size)
        op_name = Text(name,color = color_name).shift((x0+name_right_shift_offset)*RIGHT+(y0+name_up_shift_offset)*UP)
        op_name.scale(size*name_font_scale)
        
        net_point = [
            [[-1*size+x0,-1*size+y0,0],[-1*size+x0,1*size+y0,0],[1*size+x0,0*size+y0,0],[-1*size+x0,-1*size+y0,0]],
            [[-1*size+x0,0.7*size+y0,0],[-1.5*size+x0,0.7*size+y0,0]],
            [[-1*size+x0,-0.7*size+y0,0],[-1.5*size+x0,-0.7*size+y0,0]],
            [[1*size+x0 ,0*size+y0,0],[1.5*size+x0,0*size+y0,0]]
        ]
        NetList = connect_point_list(net_point,color = BLUE)
        self.play(Write(NetList.lines[0]),
                  Write(NetList.lines[1]),
                  Write(NetList.lines[2]),
                  Write(NetList.lines[3]),
                  Write(NetList.lines[4]),
                  Write(NetList.lines[5]),
                  Write(plus),Write(minus),
                  Write(op_name))'''
        
        self.wait(2)
        