from sys import exit
from lib.graph_and_vec import graph
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


if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    
    angle = 0

    matrix=[1,0,0,1]

    dpu=40
    g=graph(screen,dpu,matrix)
    clock = pygame.time.Clock()
    center_pos = [width // 2, height // 2]
    xpos=0
    ypos=0
    cam_vec=(0,0)
    
    i_hat_rot=0
    j_hat_rot=0

    text_box1=[]
    text_box1.append(Text_Box(screen,((20,252),(55,292)),3,"40"))
    text_box1.append(Text_Box(screen,((20,192),(55,232)),3,"0"))
    text_box1.append(Text_Box(screen,((155,192),(190,232)),3,"0"))

    text_box=[]
    text_box.append(Text_Box(screen,((20,72),(135,112)),11,"1"))
    text_box.append(Text_Box(screen,((155,72),(270,112)),11,"0"))
    text_box.append(Text_Box(screen,((20,132),(135,172)),11,"0"))
    text_box.append(Text_Box(screen,((155,132),(270,172)),11,"1"))

    for tt in text_box:
        tt.var_change(0)

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
                for tt in text_box:
                    tt.input1(event)
                
                for tt in text_box1:
                    tt.input2(event)
                #text_box1[0].input2(event)
                #text_box1[1].input2(event)
                #text_box1[2].input2(event)

        for tt in text_box:
            tt.update1()
        text_box1[0].update1()
        text_box1[1].update1()
        text_box1[2].update1()
        
        for tt in text_box:
            tt.update2()
        text_box1[0].update2()
        text_box1[1].update2()
        text_box1[2].update2()

        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and 20 < pygame.mouse.get_pos()[0] < 120 and 22 < pygame.mouse.get_pos()[1] < 62:
            cam_vec=(0,0)
            dpu=40
            pp = True
        
        if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and animated_c[0][0] < pygame.mouse.get_pos()[0] < animated_c[1][0] and animated_c[0][1] < pygame.mouse.get_pos()[1] < animated_c[1][1]:
            pp=True

            if animated == True:
                animated=False
                while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                    pppp = pygame.event.get()
                    for event in pppp:
                        if event.type == pygame.QUIT:
                            exit()

            elif animated == False:
                animated=True
                while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
                    pppp = pygame.event.get()
                    for event in pppp:
                        if event.type == pygame.QUIT:
                            exit()


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

        for tt in text_box:
            tt.var_change(animated_func(animated,tt.get(),tt.get_var()))


        if text_box1[0].get() == '':
            rez_t="0"
        else:
            rez_t=text_box1[0].get()

        if text_box1[1].get() == '':
            i_rot_t="0"
        else:
            i_rot_t=text_box1[1].get()

        if text_box1[2].get() == '':
            j_rot_t="0"
        else:
            j_rot_t=text_box1[2].get()


        if animated:
            if int(i_rot_t) < i_hat_rot:
                i_hat_rot-=1
            elif int(i_rot_t) > i_hat_rot:
                i_hat_rot+=1
        else:
            if text_box1[1].get()=='':
                i_hat_rot=0
            else:
                i_hat_rot=int(text_box1[1].get())


        if animated:
            if int(j_rot_t) < j_hat_rot:
                j_hat_rot-=1
            elif int(j_rot_t) > j_hat_rot:
                j_hat_rot+=1
        else:
            if text_box1[2].get()=='':
                j_hat_rot=0
            else:
                j_hat_rot=int(text_box1[2].get())


        g.new_dpu(dpu)

        t_center_pos = (width // 2, height // 2)
        
        xpos=-((-(cam_vec[0]*dpu))-t_center_pos[0])
        ypos= ((-(cam_vec[1]*dpu))-t_center_pos[1])

        center_pos[0]=xpos
        center_pos[1]=-ypos

        g.resize(center_pos)

        screen.fill((255,255,255))

        g.new_rot((int(i_hat_rot),int(j_hat_rot)))


        matrix=[
            text_box[0].get_var(),text_box[1].get_var(),
            text_box[2].get_var(),text_box[3].get_var()
            ]
        
            
        g.new_matrix(matrix)
        angle = (angle+1)%360

        g.draw_grid2((int(rez_t),int(rez_t)))

        g.add_vec_draw([2,5],[-4,1])
        g.draw_vec([4,2])
        g.draw_vec2()

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


        for tt in text_box:
            tt.show((5,10))
        text_box1[0].show((2,10))
        text_box1[1].show((2,10))
        text_box1[2].show((2,10))
        pygame.display.flip()
        clock.tick(60)
        