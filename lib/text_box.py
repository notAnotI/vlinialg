import pygame
#comic sans
class Text_Box:
    def __init__(self,screen,cords,m_length,start_text='',font='Agency FB',font_size=16):
        self.screen = screen
        self.cords = cords
        self.text = start_text
        self.font = pygame.font.SysFont(font,font_size)
        self.clicked = False
        self.m_length = m_length
    
    def input1(self,event):
        if self.clicked:
           if event.key == pygame.K_BACKSPACE:
               # stores text except last letter
               self.text = self.text[0:-1]
           elif len(list(self.text)) < self.m_length:
               if (event.unicode == "-" and len(self.text)==0) or (event.unicode == "." and "." not in self.text) or event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                   self.text += event.unicode
    
    def input2(self,event):
        if self.clicked:
           if event.key == pygame.K_BACKSPACE:
               # stores text except last letter
               self.text = self.text[0:-1]
           elif len(list(self.text)) < self.m_length:
               if event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                   self.text += event.unicode


    def update1(self):
        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and self.clicked:
            while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                pppp = pygame.event.get()
            self.clicked = False
            return True
        return False


    def update2(self):
        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and self.cords[0][0] < pygame.mouse.get_pos()[0] < self.cords[1][0] and self.cords[0][1] < pygame.mouse.get_pos()[1] < self.cords[1][1] and not self.clicked:
            while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                pppp = pygame.event.get()
            self.clicked = True
            return True
        return False
    
    def get(self):
        return self.text

    def var_change(self,var):
        self.var = var

    def get_var(self):
        return self.var

    def show(self,font_cort,b_c=[255,255,255],s_c=[100,150,100],ns_c=[100,100,100]):
        pygame.draw.rect(self.screen,b_c,[self.cords[0][0],self.cords[0][1],self.cords[1][0]-self.cords[0][0],self.cords[1][1]-self.cords[0][1]])
        text = self.font.render(self.text , True ,[0,0,0])
        self.screen.blit(text ,(font_cort[0]+self.cords[0][0],(font_cort[1]+self.cords[0][1])))
        self.screen.blit(text ,((font_cort[0]+self.cords[0][0]+1),(font_cort[1]+self.cords[0][1])))
        self.screen.blit(text ,(font_cort[0]+self.cords[0][0],((font_cort[1]+self.cords[0][1])+1)))
        #self.screen.blit(text ,((font_cort[0]+self.cords[0][0]+1),((font_cort[1]+self.cords[0][1])+1)))
        if self.clicked:
            pygame.draw.rect(self.screen,s_c,[self.cords[0][0],self.cords[0][1],self.cords[1][0]-self.cords[0][0],self.cords[1][1]-self.cords[0][1]],2)
        else:
            pygame.draw.rect(self.screen,ns_c,[self.cords[0][0],self.cords[0][1],self.cords[1][0]-self.cords[0][0],self.cords[1][1]-self.cords[0][1]],2)