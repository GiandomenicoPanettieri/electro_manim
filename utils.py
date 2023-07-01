from manim import *
from typing import cast
from NetList import *

###############################  USEFULL FUNCTIONS  #################################
def connect_terminal(n0,n1,color = WHITE):
    return Line(n0,n1,color=color)

def connect_nodes_oriented(node_list):
    local_node_list = node_list
    subnet =[]
    
    if len(node_list) == 1:
        return print("node list has less than one node")
    else:
        for i in range(0,len(local_node_list)-1):
            subnet.append(connect_terminal(local_node_list[i],local_node_list[i+1]))
    return subnet