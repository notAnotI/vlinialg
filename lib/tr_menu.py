import keyboard
import pygame
from sys import exit


class TR_menu:
    def __init__(self,screen,):
        self.screen = screen
        self.size = self.screen.get_size()
        self.hovered = False
    
    def new_screen(self,screen):
        self.screen = screen

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(num_buttons=3) == (True, False,False)
        if self.size[0]-80 < mouse[0] < self.size[0]-40 and -1 < mouse[1] < 40:
            if click:
                self.screen1 = self.screen
                global screen
                screen = pygame.display.set_mode((1,1), pygame.RESIZABLE)
                pygame.display.flip()
                keyboard.press("windows+down arrow")
                keyboard.release("windows+down arrow")
                
                max = False
                while not max:
                    pppp = pygame.event.get()
                    for event in pppp:
                        if event.type == pygame.QUIT:
                            exit()
                        if event.type == 32768:
                            max = True
                            #self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                            return True
            else:
                self.hovered1 = True
                return False
        self.hovered1 = False
        #return False
        
        if self.size[0]-40 < mouse[0] < self.size[0]+1 and -1 < mouse[1] < 40:
            if click:
                exit()
            else:
                self.hovered = True
                return False
        self.hovered = False
        return False

    def show(self):
        if self.hovered:
            pygame.draw.rect(self.screen,[170,30,30],[self.size[0]-40,0,40,40])
        else:
            pygame.draw.rect(self.screen,[250,250,250],[self.size[0]-40,0,40,40])

        if self.hovered1:
            pygame.draw.rect(self.screen,[170,30,30],[self.size[0]-80,0,40,40])
        else:
            pygame.draw.rect(self.screen,[250,250,250],[self.size[0]-80,0,40,40])

        pygame.draw.rect(self.screen,[0,0,0],[self.size[0]-82,-2,42,42],2)
        pygame.draw.rect(self.screen,[0,0,0],[self.size[0]-42,-2,42,42],2)
        pygame.draw.line(self.screen,[0,0,0],[self.size[0]-70,20],[self.size[0]-52,20],2)
        pygame.draw.line(self.screen,[0,0,0],[self.size[0]-30,10],[self.size[0]-10,30],3)
        pygame.draw.line(self.screen,[0,0,0],[self.size[0]-30,30],[self.size[0]-10,10],3)