from manim import *
from NetList import *
from components import *
from utils import *


class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        #plane = NumberPlane()
        #self.add(plane)

        #Components definitions
        Rd = R( name = "Rd", value_text="3k",
                x0=0,y0=2, size=1)
        Rd_img = Rd.get_group()

        
        Rs = R( name = "Rs", value_text="2k",
                x0=0,y0=-1.5, size=1, color_name=RED)
        Rs_img = Rs.get_group()

        Cs = C( name = "Cs", value_text = "1n",
                x0=1,y0=-1.5, size= 1
               )
        Cs_img = Cs.get_group()

        M1 = NMOSB(name = "M1", x0=-0.5 , y0=0, size=1)
        M1_img = M1.get_group()

        

        GND1 = GND(" ",0,-3,1)
        GND1_img = GND1.get_group()

        self.play(FadeIn(M1_img),FadeIn(Rd_img),
                  FadeIn(Rs_img),FadeIn(Cs_img),
                  FadeIn(GND1_img))
        
        
        #output and input nodes
        output_node = node("out",x0=1,y0=1, value_font_scale = 0.8, color=RED)
        output_node_img = output_node.get_group()
        input_node = node(" ",x0=-1,y0=0, color=RED)
        input_node_img = input_node.get_group()


        #Net List
        Net_List = Net() 

        Sub_Net1 = [
            connect_terminal(Rd.n1,M1.nd),
            connect_terminal(Rs.n0,M1.ns),
            connect_terminal(Rs.n1,GND1.n0),
            connect_terminal(Rs.n0,Cs.n0),
            connect_terminal(Rs.n1,Cs.n1),
            connect_terminal(Rd.n0,[0,3,0]),
            connect_terminal(output_node.n0,[0,1,0],color=RED)
        ]
        Sub_Net1 = Net(Sub_Net1)
        Net_List.merge_subnet(Sub_Net1)
        Net_List_img=Net.img(Net_List)

        Vdd_line = connect_terminal([-1,3,0],[1,3,0])
        Vdd = Text("Vdd",font_size=20).shift(UP*3.3)
        Vg = Text("Vg",font_size=20,color = RED).shift(LEFT*1.4)
        Net_List.add_line(Vdd_line)
        Net_List_img=Net.img(Net_List)



        #animations
        self.play(FadeIn(Net_List_img),Write(Vdd),Write(Vg),
                  FadeIn(input_node_img),FadeIn(output_node_img))

        Circuit1 = Group(Rd_img,Rs_img,Cs_img,M1_img,Vdd,Vg,input_node_img,
                    output_node_img,Net_List_img,GND1_img)
        
        self.wait(2)
        self.play(Circuit1.animate.shift(LEFT*2))
        self.play(Circuit1.animate.scale(0.7))

        self.wait(2)

        
        





        
          

        