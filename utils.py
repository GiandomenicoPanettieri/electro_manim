from manim import *
from typing import cast
from NetList import Net
from components import *

###############################  USEFULL FUNCTIONS  #################################
def connect_terminal(n0,n1,color = WHITE):
    return Line(n0,n1,color=color)

def connect_oriented(node_list):
    local_node_list = node_list
    subnet =[]
    
    if len(node_list) == 1:
        return print("node list has less than one node")
    else:
        for i in range(0,len(local_node_list)-1):
            subnet.append(connect_terminal(local_node_list[i],local_node_list[i+1]))
    return subnet


def connect_point_list (net_array):
    local_net_list = Net()
    if len(net_array) == 1 : 
        return Net(connect_oriented(net_array[0]))
    else:
        for i in range(0,len(net_array)):
            local_net_list.merge_subnet(Net(connect_oriented(net_array[i]))) 
    return local_net_list

def rotate_img(comp, angle, about_point):
        component = cast(component, comp)
        component.img.rotate(angle,about_point)
        component.n0 = component.n0+[component.size*component.n0[2]*np.sin(angle),
                           component.size*component.n0[2]*np.cos(angle)-component.n0[2],
                           0]
        return component