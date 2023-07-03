from manim import *
from typing import cast
from NetList import *
from utils import *

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
    def __init__(self, name, x0,y0,size,value_text, color_name , color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.size = size
        self.value_text = value_text
        self.name_font_scale = name_font_scale
        self.value_font_scale = value_font_scale
        self.name_right_shift_offset = name_right_shift_offset
        self.value_right_shift_offset = value_right_shift_offset
        self.name_up_shift_offset = name_up_shift_offset
        self.value_up_shift_offset = value_up_shift_offset
        self.color_name = color_name
        self.color_value = color_value

        self.name = Text(
            name,
            font_size = 30*size*name_font_scale,
            color = color_name
        )

        self.name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))

################################ RESISTOR ##################################

class R(component):
    def __init__(self, name, x0,y0,size,value_text= " ",
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.value = Text(
            value_text,
            font_size = 30*size*value_font_scale,
            color=color_value
        )
        
        self.value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.img = ImageMobject("texture\R").scale(0.1756442432*size)
        self.img = self.img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
        self.n1 = (rot_mat @ (n1-center))+center


    def get_group(self):
        return Group(self.img,self.name,self.value)

        
    
################################ CAPACITOR ##################################

class C(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.value_text=value_text

        self.value = Text(
            value_text,
            font_size = 30*size*value_font_scale,
            color= color_value
        )

        self.value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.img = ImageMobject("texture\C").scale(0.1642335766*size)
        self.img = self.img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
        self.n1 = (rot_mat @ (n1-center))+center


    
    def get_group(self):
        return Group(self.img,self.name,self.value)

#################################  INDUCTOR ################################
class L(component):
    def __init__(self, name, x0,y0,size,value_text = "",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.value = Text(
            value_text,
            font_size = 30*size*value_font_scale,
            color = color_value
        )

        self.value.shift(DOWN*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))

        self.img = ImageMobject("texture\L").scale(0.1735218509*size)  
        self.img = self.img.shift(RIGHT*x0+UP*y0)
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
        self.n1 = (rot_mat @ (n1-center))+center

    
    def get_group(self):
        return Group(self.img,self.name,self.value)
    

#################################  TRANSISTOR ################################
class NMOSA(component):
    def __init__(self, name, x0,y0,size,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*0.5*size)

        self.img = ImageMobject("texture\\nmos1").scale(0.1175*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.nd = [x0+0.5*size, y0+0.5*size, 0]
        self.ns = [x0+0.5*size, y0-0.5*size, 0]
        self.ng = [x0-0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nd = np.array(self.nd)
        ns = np.array(self.ns)
        ng = np.array(self.ng)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nd = (rot_mat @ (nd-center))+center
        self.ns = (rot_mat @ (ns-center))+center
        self.ng = (rot_mat @ (ng-center))+center
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nd = np.array(self.nd)
        ns = np.array(self.ns)
        ng = np.array(self.ng)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nd = (rot_mat @ (nd-center))+center
        self.ns = (rot_mat @ (ns-center))+center
        self.ng = (rot_mat @ (ng-center))+center

    
    def get_group(self):
        return Group(self.img,self.name)

class NMOSB(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*(-1.5)*size)

        self.img = ImageMobject("texture\\nmos2").scale(0.1175*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.nd = [x0-0.5*size, y0+0.5*size, 0]
        self.ns = [x0-0.5*size, y0-0.5*size, 0]
        self.ng = [x0+0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nd = np.array(self.nd)
        ns = np.array(self.ns)
        ng = np.array(self.ng)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nd = (rot_mat @ (nd-center))+center
        self.ns = (rot_mat @ (ns-center))+center
        self.ng = (rot_mat @ (ng-center))+center
    
    def get_group(self):
        return Group(self.img,self.name)
    


class PMOSA(component):
    def __init__(self, name, x0,y0,size,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*0.5*size)

        self.img = ImageMobject("texture\pmos1").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.ns = [x0+0.5*size, y0+0.5*size, 0]
        self.nd = [x0+0.5*size, y0-0.5*size, 0]
        self.ng = [x0-0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nd = np.array(self.nd)
        ns = np.array(self.ns)
        ng = np.array(self.ng)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nd = (rot_mat @ (nd-center))+center
        self.ns = (rot_mat @ (ns-center))+center
        self.ng = (rot_mat @ (ng-center))+center
    
    def get_group(self):
        return Group(self.img,self.name)

class PMOSB(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*(-1.5)*size)

        self.img = ImageMobject("texture\pmos2").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.ns = [x0-0.5*size, y0+0.5*size, 0]
        self.nd = [x0-0.5*size, y0-0.5*size, 0]
        self.ng = [x0+0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nd = np.array(self.nd)
        ns = np.array(self.ns)
        ng = np.array(self.ng)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nd = (rot_mat @ (nd-center))+center
        self.ns = (rot_mat @ (ns-center))+center
        self.ng = (rot_mat @ (ng-center))+center
    
    def get_group(self):
        return Group(self.img,self.name)
    

class NPNA(component):
    def __init__(self, name, x0,y0,size,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*0.5*size)

        self.img = ImageMobject("texture\\npn1").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.nc = [x0+0.5*size, y0+0.5*size, 0]
        self.ne = [x0+0.5*size, y0-0.5*size, 0]
        self.nb = [x0-0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nc = np.array(self.nc)
        ne = np.array(self.ne)
        nb = np.array(self.nb)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nc = (rot_mat @ (nc-center))+center
        self.ne = (rot_mat @ (ne-center))+center
        self.nb = (rot_mat @ (nb-center))+center
    
    def get_group(self):
        return Group(self.img,self.name)

class NPNB(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*(-1.5)*size)

        self.img = ImageMobject("texture\\npn2").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.nc = [x0-0.5*size, y0+0.5*size, 0]
        self.ne = [x0-0.5*size, y0-0.5*size, 0]
        self.nb = [x0+0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nc = np.array(self.nc)
        ne = np.array(self.ne)
        nb = np.array(self.nb)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nc = (rot_mat @ (nc-center))+center
        self.ne = (rot_mat @ (ne-center))+center
        self.nb = (rot_mat @ (nb-center))+center
    
    
    def get_group(self):
        return Group(self.img,self.name)
    

class PNPA(component):
    def __init__(self, name, x0,y0,size,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*0.5*size)

        self.img = ImageMobject("texture\pnp1").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.ne = [x0+0.5*size, y0+0.5*size, 0]
        self.nc = [x0+0.5*size, y0-0.5*size, 0]
        self.nb = [x0-0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nc = np.array(self.nc)
        ne = np.array(self.ne)
        nb = np.array(self.nb)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nc = (rot_mat @ (nc-center))+center
        self.ne = (rot_mat @ (ne-center))+center
        self.nb = (rot_mat @ (nb-center))+center
    
    
    def get_group(self):
        return Group(self.img,self.name)

class PNPB(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)

        self.name.shift(RIGHT*(-1.5)*size)

        self.img = ImageMobject("texture\pnp2").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.ne = [x0-0.5*size, y0+0.5*size, 0]
        self.nc = [x0-0.5*size, y0-0.5*size, 0]
        self.nb= [x0+0.5*size, y0, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        nc = np.array(self.nc)
        ne = np.array(self.ne)
        nb = np.array(self.nb)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.nc = (rot_mat @ (nc-center))+center
        self.ne = (rot_mat @ (ne-center))+center
        self.nb = (rot_mat @ (nb-center))+center
    
    
    def get_group(self):
        return Group(self.img,self.name)
    




#################################  SCRS ################################
class V(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)


        self.value = Text(
            value_text,
            font_size = 30*size*value_font_scale,
            color = color_value
        )

        self.value.shift(DOWN*0.25*size
                          +RIGHT*(-0.6)*size
                          +RIGHT*(x0+value_right_shift_offset)
                          +UP*(y0+value_up_shift_offset))
        self.name.shift(RIGHT*(-1.1)*size)

        self.img = ImageMobject("texture\V").scale(0.16981132075471698113207547169811*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
        self.n1 = (rot_mat @ (n1-center))+center
            
    def get_group(self):
        return Group(self.img,self.name, self.value)
    
class A(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)


        self.value = Text(
            value_text,
            font_size = 30*size*value_font_scale,
            color = color_value
        )

        self.value.shift(DOWN*0.25*size
                          +RIGHT*(-0.6)*size
                          +RIGHT*(x0+value_right_shift_offset)
                          +UP*(y0+value_up_shift_offset))
        self.name.shift(RIGHT*(-1.1)*size)

        self.img = ImageMobject("texture\A").scale(0.15089880304678998911860718171926*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.n0 = [x0, y0+0.5*size, 0]
        self.n1 = [x0, y0-0.5*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
        self.n1 = (rot_mat @ (n1-center))+center
            
    def get_group(self):
        return Group(self.img,self.name, self.value)

#################################  GROUND ################################
class GND(component):
    def __init__(self, name, x0,y0,size,value_text= " ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name, color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset )

        self.img = ImageMobject("texture\gnd").scale(0.16687268232385661310259579*0.5*size)  
        self.img = self.img.shift(RIGHT*x0+UP*(y0))
        self.n0 = [x0, y0+0.25*size, 0]
        self.size = size
        self.center = [x0,y0,0]
    
    def rotate_component(self, angle):
        self.img = self.img.rotate(angle = angle, about_point = self.center)
        
        n0 = np.array(self.n0)
        n1 = np.array(self.n1)
        center = np.array(self.center) 
        rot_mat = np.array([
            [np.cos(angle),(-1)*np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0, 0, 1]
        ])
        self.n0 = (rot_mat @ (n0-center))+center
    
    def get_group(self):
        return Group(self.img,self.name)
    
###############################         NODE         ################################
class node(component):
    def __init__(self, name, x0,y0,size=1,value_text=" ",name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0, color=WHITE,
                 color_name = WHITE, color_value = WHITE):
        component.__init__(self, name, x0,y0,size,value_text,
                 color_name , color_value,
                 name_font_scale,value_font_scale,
                 name_right_shift_offset,value_right_shift_offset,
                 name_up_shift_offset,value_up_shift_offset)
        
        self.name = Text(
            name,
            font_size = 30*size*name_font_scale,
            color = color
        )

        self.name.shift(UP*0.25*size
                          +RIGHT*(0.25)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))
        self.img = Dot(color=color).shift(RIGHT*(x0)
                                            +UP*(y0))
    
        self.n0 = [x0, y0, 0]
    
    def get_group(self):
        return Group(self.dot,self.name)

