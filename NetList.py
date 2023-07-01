from manim import *
from typing import cast
from utils import *

class Net():
    def __init__(self, lines = []):
        self.lines = lines
    
    '''def assign_net(self, line_list): 
        self.lines = line_list'''
    
    def add_line(self, line): #adds a single line to net
        self.lines.append(line)
    
    def merge_subnet(self, new_list): #merges two subnets
        new_list = cast(Net, new_list)
        self.lines = self.lines + cast(Net,new_list).lines

    def net_length(self):
        return len(self.lines)
    
    def net_mobject(self):
        net_list_object_temp = self.lines[0]
        if len(self.lines) == 1 :
            return net_list_object_temp
        else:
            for i in range(1, len(self.lines)):
                net_list_object = Group(net_list_object_temp,self.lines[i])
                net_list_object_temp = net_list_object
            return net_list_object
        

