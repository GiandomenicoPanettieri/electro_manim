from manim import *
from typing import cast

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
        



############################### COMPONENT CLASS ##############################
'''
V1.1 components available are 
    R   resistor
    C   capacitor
    L   inductor

each component has usefull parameters for animation. Some of those are mandatory
    
    --MANDATORY PARAMETERS FOR COMPONENTS--
    name                        name in the animation of the component
    value_text                  value of the main physiscal property. if no, give " " 
    x0,y0                       center coordinates
    size        
    --NOT MANDATORY PARAMETERS--
    name_font_scale             resizes the name in the animation
    value_font_scale            resizes the value in the animation
    name_right_shift_offset
    value_right_shift_offset
    name_up_shift_offset
    value_right_shift_offset     


to get the group of the component+name+value as a Mobject, the method get_group()
is required. Moreover, each component comes with the location in the plane of
the terminals (nodes n1, n2)

'''

class component():
    def __init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.size=size
        self.value_text=value_text
        self.name_font_scale=name_font_scale
        self.value_font_scale=value_font_scale
        self.name_right_shift_offset=name_right_shift_offset
        self.value_right_shift_offset=value_right_shift_offset
        self.name_up_shift_offset=name_up_shift_offset
        self.value_up_shift_offset=value_up_shift_offset

        self.name = Text(
            name,
            font_size = 30*size*name_font_scale,
        )

        self.name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))

################################ RESISTOR ##################################

class R(component):
    def __init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.R_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )
        
        self.R_value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.R_img = ImageMobject("texture\R").scale(0.1746442432*size)
        self.R_img = self.R_img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
    
    def get_group(self):
        return Group(self.R_img,self.name,self.R_value)
    
################################ CAPACITOR ##################################

class C(component):
    def __init__(self, name, x0,y0,size,value_text,name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.value_text=value_text

        self.C_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )

        self.C_value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.C_img = ImageMobject("texture\C").scale(0.1642335766*size)
        self.C_img = self.C_img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
    
    def get_group(self):
        return Group(self.C_img,self.name,self.C_value)

#################################  INDUCTOR ################################
class L(component):
    def __init__(self, name, x0,y0,size,value_text,name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.L_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )

        self.name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))

        self.L_img = ImageMobject("texture\L").scale(0.1735218509*size)  
        self.L_img = self.L_img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
    
    def get_group(self):
        return Group(self.L_img,self.name,self.L_value)
    

#################################  NMOS ################################
class NMOS(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.name.shift(RIGHT*1
                        +RIGHT*(x0+name_right_shift_offset)
                        +UP*(y0+name_up_shift_offset))

        self.NMOS_img = ImageMobject("texture\\nmos1").scale(0.1175*size)  
        self.NMOS_img = self.NMOS_img.shift(RIGHT*x0+UP*(y0))
        self.nd = [x0+0.5*size, y0+0.5*size, 0]
        self.ns = [x0+0.5*size, y0-0.5*size, 0]
        self.ng = [x0-0.5*size, y0, 0]
    
    def get_group(self):
        return Group(self.NMOS_img,self.name)

#################################  GROUND ################################
class GND(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.GND_img = ImageMobject("texture\gnd").scale(0.16687268232385661310259579*0.5*size)  
        self.GND_img = self.GND_img.shift(RIGHT*x0+UP*(y0))
        self.n0 = [x0, y0+0.25*size, 0]
    
    def get_group(self):
        return Group(self.GND_img,self.name)
    
###############################         NODE         ################################
class node(component):
    def __init__(self, name, x0,y0,size=1,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0, color=WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)
        
        self.node_name = Text(
            name,
            font_size = 30*size*name_font_scale,
            color = color
        )

        self.node_name.shift(UP*0.25*size
                          +RIGHT*(0.25)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))
        self.my_dot = Dot(color=color).shift(RIGHT*(x0+name_right_shift_offset)
                                            +UP*(y0+name_up_shift_offset))
    
        self.n0 = [x0, y0, 0]
    
    def get_group(self):
        return Group(self.my_dot,self.node_name)
    

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
