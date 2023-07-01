from manim import *

class circuit():

    def resonator(Lname,Cname,Rname,Lvalue,Cvalue,Rvalue):
        line1= Line((-2.023,1,0), (2,1,0))  #top_line
        line2= Line((-2.025,-1,0),(2,-1,0)) #bottom_line

        L1 = ImageMobject("texture\L").shift(RIGHT*2.08)
        L1 = L1.scale(0.35)
        textL1 = Text(Lname+"\n"+Lvalue,
                    font_size = 40).shift(RIGHT*3)
        
        C1 = ImageMobject("texture\C").shift(LEFT*2)
        C1 = C1.scale(0.33)       
        textC1 = Text(Cname+"\n"+Cvalue,
                    font_size = 40).shift(LEFT*1)
        
        R1 = ImageMobject("texture\R").scale(0.35)
        textR1 = Text(Rname+"\n"+Rvalue,
                    font_size = 40).shift(RIGHT*1)
        
        return Group(L1,C1,R1,line1,line2,textR1,textC1,textL1)
    

class animated_circuit(Scene):
    def animated_resonator(self, Lname,Cname,Rname,Lvalue,Cvalue,Rvalue):
        #optional plane to get a reference
        #plane = NumberPlane()
        #self.add(plane)

        line1= Line((-2.023,1,0), (2,1,0))  #top_line
        line2= Line((-2.025,-1,0),(2,-1,0)) #bottom_line

        #inductor, resistor and capacitor full definition
        L1 = ImageMobject("texture\L")
        textL1 = Text(Lname+"\n"+Lvalue,
                        font_size = 40)
        
        C1 = ImageMobject("texture\C")          
        textC1 = Text(Cname+"\n"+Cvalue,
                        font_size = 40)
        
        R1 = ImageMobject("texture\R")
        textR1 = Text(Rname+"\n"+Rvalue,
                        font_size = 40)
        
        self.play(FadeIn(L1), run_time=0.3)
        self.play(L1.animate.shift(RIGHT*2.08), run_time = 0.3)
        self.play(L1.animate.scale(0.35), run_time=0.3)

        self.play(FadeIn(C1), run_time=0.3)
        self.play(C1.animate.shift(LEFT*2), run_time = 0.3)
        self.play(C1.animate.scale(0.33), run_time=0.3)

        self.play(FadeIn(R1), run_time=0.3)
        self.play(R1.animate.scale(0.35), run_time=0.3)

        self.play(Write(line1), run_time=0.3)
        self.play(Write(line2), run_time=0.3)

        self.play(Write(textL1), run_time=0.3)
        self.play(textL1.animate.shift(RIGHT*3), run_time = 0.3)
        self.play(Write(textC1), run_time=0.3)
        self.play(textC1.animate.shift(LEFT*1), run_time = 0.3)
        self.play(Write(textR1), run_time=0.3)
        self.play(textR1.animate.shift(RIGHT*1), run_time = 0.3)
        return Group(L1,C1,R1,line1,line2,textR1,textC1,textL1)

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
        


class R(component):
    def __init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.R_name = Text(
            name,
            font_size = 30*size*name_font_scale
        )

        self.R_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )
        
        self.R_name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))
        self.R_value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.R_img = ImageMobject("texture\R").scale(0.1746442432*size)
        self.R_img = self.R_img.shift(RIGHT*x0+UP*y0)
        self.n1 = [x0, y0+0.5*size]
        self.n2 = [x0, y0-0.5*size]
    
    def get_group(self):
        return Group(self.R_img,self.R_name,self.R_value)
    


class C(component):
    def __init__(self, name, x0,y0,size,value_text,name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)

        self.value_text=value_text

        self.C_name = Text(
            name,
            font_size = 30*size*name_font_scale
        )

        self.C_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )

        self.C_name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))
        self.C_value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))

        self.C_img = ImageMobject("texture\C").scale(0.1642335766*size)
        self.C_img = self.C_img.shift(RIGHT*x0+UP*y0)
        self.n1 = [x0, y0+0.5*size]
        self.n2 = [x0, y0-0.5*size]
    
    def get_group(self):
        return Group(self.C_img,self.C_name,self.C_value)

class L(component):
    def __init__(self, name, x0,y0,size,value_text,name_font_scale=1,
                 value_font_scale=1,name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0):
        component.__init__(self, name, x0,y0,size,value_text,
                 name_font_scale=1,value_font_scale=1,
                 name_right_shift_offset=0,value_right_shift_offset=0,
                 name_up_shift_offset=0,value_up_shift_offset=0)
        
        self.L_name = Text(
            name,
            font_size = 30*size*name_font_scale
        )

        self.L_value = Text(
            value_text,
            font_size = 30*size*value_font_scale
        )

        self.L_name.shift(UP*0.25*size
                          +RIGHT*(0.5)*size
                          +RIGHT*(x0+name_right_shift_offset)
                          +UP*(y0+name_up_shift_offset))
        self.L_value.shift(DOWN*0.25*size
                           +RIGHT*0.5*size
                           +RIGHT*(x0+value_right_shift_offset)
                           +UP*(y0+value_up_shift_offset))
        self.L_img = ImageMobject("texture\L").scale(0.1735218509*size)  
        self.L_img = self.L_img.shift(RIGHT*x0+UP*y0)
        self.n1 = [x0, y0+0.5*size]
        self.n2 = [x0, y0-0.5*size]
    
    def get_group(self):
        return Group(self.L_img,self.L_name,self.L_value)

