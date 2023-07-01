from manim import *
from NetList import *
from components import *
from utils import *

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

        
        net_list = Net()

        line_list = [
            connect_terminal(M1.nd,Rd.n1),
            connect_terminal([0,1,0],[-1,1,0])
        ]
        sub_net_1 = Net(line_list)
        
        line_list = connect_nodes_oriented(
            [[0,1,0],
            [1,1,0]]
        )
        sub_net_2 = Net(line_list)

        net_list.merge_subnet(sub_net_1)
        net_list.merge_subnet(sub_net_2)

        net_list_img=net_list.net_mobject()
        self.add(net_list_img)





        
          

        