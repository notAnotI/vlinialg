from sys import exit
from lib.graph_and_vec import graph
from lib.text_box import Text_Box 
import pygame
from lib.matrix import Matrix


def wait():
    while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
        pppp = pygame.event.get()
        for event in pppp:
            if event.type == pygame.QUIT:
                exit()



if __name__ == "__main__":
    pygame.init()
    size = width, height = 0, 0
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    size = width, height = screen.get_size()
    print(size)
    angle = 0

    matrix=[1,0,0,1]

    dpu=40
    g=graph(screen,dpu,matrix)
    clock = pygame.time.Clock()
    center_pos = [width // 2, height // 2]
    xpos=0
    ypos=0
    cam_vec=(0,0)

    rez_text_box = Text_Box(screen,((20,252),(55,292)),3,"40")

    m=Matrix(screen,size)

    lfc=False

    last_corts=(400,400)

    animated=False
    animated_c=((155,22),(255,62))
    smallfont = pygame.font.SysFont('comic sans',16)
    text = smallfont.render('reset cam' , True ,[0,0,0])
    while True:
        pp=False
        pppp = pygame.event.get()
        for event in pppp:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.dict["size"]
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                center_pos = [width // 2, height // 2]
                g.resize(center_pos)
            elif event.type == pygame.WINDOWMAXIMIZED:
                WSIZE = (0,0)
                flags = pygame.FULLSCREEN
                screen = pygame.display.set_mode(WSIZE, flags)
                width, height = screen.get_size()
                t_center_pos = [width // 2, height // 2]
            elif event.type == 32777:
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                t_center_pos = [width // 2, height // 2]

            elif event.type == pygame.MOUSEWHEEL:
               dpu += event.y*(dpu/10)
            
            elif event.type == pygame.KEYDOWN:
                m.input(event)             
                rez_text_box.input1(event)

        rez_text_box.update1()
        m.update1()
        m.update2()
        rez_text_box.update2()

        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and 20 < pygame.mouse.get_pos()[0] < 120 and 22 < pygame.mouse.get_pos()[1] < 62:
            cam_vec=(0,0)
            dpu=40
            pp = True
        
        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and animated_c[0][0] < pygame.mouse.get_pos()[0] < animated_c[1][0] and animated_c[0][1] < pygame.mouse.get_pos()[1] < animated_c[1][1]:
            pp=True

            if animated == True:
                animated=False
                wait()

            elif animated == False:
                animated=True
                wait()


        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and lfc == True and pp == False:
            cam_vec=(cam_vec[0]+((pygame.mouse.get_pos()[0]-(last_corts[0]))/dpu),(cam_vec[1]+((pygame.mouse.get_pos()[1]-(last_corts[1]))/dpu)))
            pp=True
            last_corts=pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and lfc == False and pp == False:
            lfc = True
            last_corts=pygame.mouse.get_pos()
            pp=True
        if lfc == True and pp == False:
            lfc = False
            pp=True

        if rez_text_box.get() == '':
            rez_t="0"
        else:
            rez_t=rez_text_box.get()

        m.update3(animated)
        
        mm = m.get_matrix()

        g.new_dpu(dpu)

        t_center_pos = (width // 2, height // 2)
        
        xpos=-((-(cam_vec[0]*dpu))-t_center_pos[0])
        ypos= ((-(cam_vec[1]*dpu))-t_center_pos[1])

        center_pos[0]=xpos
        center_pos[1]=-ypos

        g.resize(center_pos)

        screen.fill((255,255,255))

        g.new_rot((int(mm[4]),int(mm[5])))


        matrix=[
            mm[0],mm[1],
            mm[2],mm[3]
            ]
        
            
        g.new_matrix(matrix)
        angle = (angle+1)%360

        g.draw_grid2((int(rez_t),int(rez_t)))

        g.add_vec_draw([2,5],[-4,1])
        #g.draw_vec([4,2])
        #g.draw_vec2()

        if 20 < pygame.mouse.get_pos()[0] < 120 and 22 < pygame.mouse.get_pos()[1] < 62:
            pygame.draw.rect(screen,[200,200,200],[20,22,100,40])
        else:
            pygame.draw.rect(screen,[150,150,150],[20,22,100,40])
        screen.blit(text , (25,27))
#my cat typed this
#wsEDXCRFzszaxdwe+

        if animated:
            pygame.draw.rect(screen,[100,180,100],[animated_c[0][0],animated_c[0][1],animated_c[1][0]-animated_c[0][0],animated_c[1][1]-animated_c[0][1]])
        else:
            pygame.draw.rect(screen,[100,100,180],[animated_c[0][0],animated_c[0][1],animated_c[1][0]-animated_c[0][0],animated_c[1][1]-animated_c[0][1]])


        rez_text_box.show((2,10))
        m.show()

        pygame.display.flip()
        clock.tick(60)
        