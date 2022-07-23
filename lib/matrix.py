from lib.text_box import Text_Box
import pygame

def animated_func(anim,user_text,user_int):
    if anim:
        if user_text == '' or user_text == '-' or user_text == '.':
            if user_int < 0:
                user_int += (0-user_int)/20
            if user_int > 0:
                user_int -= (user_int-0)/20
        else:
            if user_int < float(user_text):
                user_int += (float(user_text)-user_int)/20
            if user_int > float(user_text):
                user_int -= (user_int-float(user_text))/20
    else:
        if user_text == '' or user_text == '-' or user_text == '.' or user_text == '-.':
            user_int = 0
        else:
            user_int = float(user_text)
    return user_int

def animated_func2(animated,text_box,rot):
    if text_box == '':
        rot_t="0"
    else:
        rot_t=text_box

    if animated:
        if int(rot_t) < rot:
            rot-=1
        elif int(rot_t) > rot:
            rot+=1
    else:
        if text_box=='':
            rot=0
        else:
            rot=int(text_box)
    return rot
    
class Matrix:
    def __init__(self,screen,size):
        self.size = size
        self.screen = screen
        self.text_box=[]
        self.text_box.append(Text_Box(screen,((95,size[1]-112),(142,size[1]-72)),6,"1"))  #[0]         
        self.text_box.append(Text_Box(screen,((95,size[1]-172),(142,size[1]-132)),6,"0")) #[1]    [1][3]
        self.text_box.append(Text_Box(screen,((20,size[1]-112),(67,size[1]-72)),6,"0"))    #[2]    [0][2]
        self.text_box.append(Text_Box(screen,((20,size[1]-172),(67,size[1]-132)),6,"1"))  #[3]         
        
        self.text_box.append(Text_Box(screen,((20,size[1]-62),(55,size[1]-22)),3,"0"))     #[4]       [4][5]
        self.text_box.append(Text_Box(screen,((105,size[1]-62),(140,size[1]-22)),3,"0"))  #[5]

        for t in self.text_box:
            t.var_change(0)

        self.activate = False
    
    def input(self, event):
        self.text_box[0].input1(event)
        self.text_box[1].input1(event)
        self.text_box[2].input1(event)
        self.text_box[3].input1(event)
        
        self.text_box[4].input2(event)
        self.text_box[5].input2(event)

    def new_screen(self,screen):
        for t in self.text_box:
            t.new_screen(screen)
        self.screen = screen

    def update1(self):
        for t in self.text_box:
            pp = t.update1()
        return pp

    def update2(self):
        pp2 = False
        pp = False
        if self.activate:
            for t in self.text_box:
                pp1 = t.update2()
                if pp1:
                    pp2 = True
                    pp = True
            if not pp2:
                pp = False
                if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and 140 < pygame.mouse.get_pos()[0] < 160 and self.size[1]-198 < pygame.mouse.get_pos()[1] < self.size[1]-178:
                    while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                        pppp = pygame.event.get()
                    self.activate = False
                    pp = True
            return pp

        else:
            if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and -1 < pygame.mouse.get_pos()[0] < 25 and self.size[1]-200 < pygame.mouse.get_pos()[1] < self.size[1]:
                while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                    pppp = pygame.event.get()
                self.activate = True
                return True
            return False
    
    def update3(self,animated):
        self.text_box[0].var_change(animated_func(animated,self.text_box[0].get(),self.text_box[0].get_var()))
        self.text_box[1].var_change(animated_func(animated,self.text_box[1].get(),self.text_box[1].get_var()))
        self.text_box[2].var_change(animated_func(animated,self.text_box[2].get(),self.text_box[2].get_var()))
        self.text_box[3].var_change(animated_func(animated,self.text_box[3].get(),self.text_box[3].get_var()))

        self.text_box[4].var_change(animated_func2(animated,self.text_box[4].get(),self.text_box[4].get_var()))
        self.text_box[5].var_change(animated_func2(animated,self.text_box[5].get(),self.text_box[5].get_var()))
        
    def get_matrix(self):
        x=[]
        for t in self.text_box:
            x.append(t.get_var())
        return x
    
    def show(self):
        if self.activate:
            pygame.draw.rect(self.screen,(250,250,250),(0,self.size[1]-200,162,200))
            pygame.draw.rect(self.screen,(0,0,0),(-5,self.size[1]-200,167,205),2)
            pygame.draw.rect(self.screen,(200,200,200),(140,self.size[1]-198,20,20))

            pygame.draw.line(self.screen,(0,0,0),(139,self.size[1]-179),(160,self.size[1]-179),2)
            pygame.draw.line(self.screen,(0,0,0),(139,self.size[1]-179),(139,self.size[1]-199),2)

            pygame.draw.line(self.screen,(0,0,0),(140,self.size[1]-189),(150,self.size[1]-199),3)
            pygame.draw.line(self.screen,(0,0,0),(140,self.size[1]-189),(150,self.size[1]-179),3)
            pygame.draw.line(self.screen,(0,0,0),(150,self.size[1]-189),(160,self.size[1]-199),3)
            pygame.draw.line(self.screen,(0,0,0),(150,self.size[1]-189),(160,self.size[1]-179),3)
            #pygame.draw.line(self.screen,(0,0,0),(0,self.size[1]-200),(162,self.size[1]-200),2)
            for t in self.text_box:
                t.show((2,10))
        else:
            pygame.draw.rect(self.screen,(255,250,250),(0,self.size[1]-200,20,200))
            pygame.draw.rect(self.screen,(0,0,0),(-5,self.size[1]-200,25,205),2)
