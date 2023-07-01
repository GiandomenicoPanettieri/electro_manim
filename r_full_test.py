from manim import *
from ELECTRONIC_MANIM import *

#

class Myscene(Scene): 

    def construct(self):
        #optional plane to get a cartesian system of coordinates
        plane = NumberPlane()
        self.add(plane)

        Rd = R( name = "Rd", value_text="3k",
                x0=0,y0=2, size=1)
        Rd_img = Rd.get_group()
        self.add(Rd_img)

        M1 = NMOS(name = "M1", x0=-0.5 , y0=0, size=1)
        M1_img = M1.get_group()
        self.add(M1_img)

        Net_List = [
            connect_terminal(Rd.n1,M1.nd),
            connect_terminal(M1.ng,[-1,1,0]),
            connect_terminal([-1,1,0],[0,1,0])
        ]
        net_img = net_mobject(Net_List)
        self.add(net_img)       