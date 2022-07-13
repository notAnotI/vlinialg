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
        if user_text == '' or user_text == '-' or user_text == '.':
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
            self.text_box.append(Text_Box(screen,((20,72),(135,112)),11,"1"))    #[0]    
            self.text_box.append(Text_Box(screen,((155,72),(270,112)),11,"0"))  #[1]         [0][1]
            self.text_box.append(Text_Box(screen,((20,132),(135,172)),11,"0"))  #[2]         [2][3]
            self.text_box.append(Text_Box(screen,((155,132),(270,172)),11,"1")) #[3]

            self.text_box.append(Text_Box(screen,((20,192),(55,232)),3,"0"))     #[4]         [4][5]
            self.text_box.append(Text_Box(screen,((155,192),(190,232)),3,"0"))  #[5]

            for t in self.text_box:
                t.var_change(0)
    
    def input(self, event):
        self.text_box[0].input1(event)
        self.text_box[1].input1(event)
        self.text_box[2].input1(event)
        self.text_box[3].input1(event)
        
        self.text_box[4].input2(event)
        self.text_box[5].input2(event)

    def update1(self):
        for t in self.text_box:
            pp = t.update1()
        return pp

    def update2(self):
        for t in self.text_box:
            pp = t.update2()
        return pp
    
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
        self.text_box[0].show((5,10))	
        self.text_box[1].show((5,10))	
        self.text_box[2].show((5,10))	
        self.text_box[3].show((5,10))	

        self.text_box[4].show((2,10))	
        self.text_box[5].show((2,10))	

if __name__ == '__main__':
    pygame.init()
    size = width, height = 0, 0
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    size = width, height = screen.get_size()
    m = Matrix(screen, size)
    while True:
        pp=False
        pppp = pygame.event.get()
        for event in pppp:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                m.input(event)
        screen.fill((255,255,255))

        if not pp:
            pp = m.update1()
        if not pp:
            pp = m.update2()
        m.update3(True)
        m.get_matrix()

        m.show()

        pygame.display.flip()