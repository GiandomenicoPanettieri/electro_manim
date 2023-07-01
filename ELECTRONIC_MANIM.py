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

class component():
    def __init__(self, name, x0,y0,size):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.size=size
        
class R(component):
    def __init__(self, name, x0,y0,size,value_text):
        component.__init__(self, name, x0,y0,size)
        self.value_text=value_text
        self.R_name = Text(
            name+"\n"+value_text,
            font_size = 30
        )
        self.R_name.shift(RIGHT*1)
        self.R_img = ImageMobject("texture\R").scale(0.18*size)
        self.R_img = self.R_img.shift(RIGHT*0.014)
        self.n1 = [x0, y0+0.5*size]
        self.n2 = [x0, y0-0.5*size]
    
    def get_group(self):
        return Group(self.R_img,self.R_name)

