from sys import exit
from lib.graph_and_vec import graph
import pygame



def collision1(clicked):
    if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and clicked:
        while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
            pppp = pygame.event.get()
        return True,False
    return False,clicked

def collision2(cords, clicked):
    if pygame.mouse.get_pressed(num_buttons=3) == (True, False,False) and cords[0][0] < pygame.mouse.get_pos()[0] < cords[1][0] and cords[0][1] < pygame.mouse.get_pos()[1] < cords[1][1] and not clicked:
        while pygame.mouse.get_pressed(num_buttons=3) == (True, False,False):
            pppp = pygame.event.get()
        return True,True
    return False,clicked
        

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

    rez_clikt=False
    rez_c=((20,252),(55,292))
    rez = "40"

    i_rot_clikt=False
    i_rot_c=((20,192),(55,232))
    i_rot = "0"

    j_rot_clikt=False
    j_rot_c=((155,192),(190,232))
    j_rot = "0"
    
    i_hat_rot=0
    j_hat_rot=0

    lfc=False
    box1=((20,72),(135,112))
    box2=((155,72),(270,112))
    box3=((20,132),(135,172))
    box4=((155,132),(270,172))
    box_clikt=False
    box_clikt1=False
    box_clikt2=False
    box_clikt3=False
    last_corts=(400,400)
    user_text = '1'
    user_text1 = '0'
    user_text2 = '0'
    user_text3 = '1'
    user_int=1
    user_int1=0
    user_int2=0
    user_int3=1
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
                if box_clikt:
                    if event.key == pygame.K_BACKSPACE:
                        
                        # stores text except last letter
                        user_text = user_text[0:-1]
                    elif len(list(user_text)) < 11:
                        if (event.unicode == "-" and len(user_text)==0) or (event.unicode == "." and "." not in user_text) or event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            user_text += event.unicode
                
                elif rez_clikt:
                    if event.key == pygame.K_BACKSPACE:
                        # stores text except last letter
                        rez = rez[0:-1]
                    elif len(list(rez)) < 3:
                        if event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            rez += event.unicode

                elif i_rot_clikt:
                    if event.key == pygame.K_BACKSPACE:
                        # stores text except last letter
                        i_rot = i_rot[0:-1]
                    elif len(list(i_rot)) < 3:
                        if event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            i_rot += event.unicode

                elif j_rot_clikt:
                    if event.key == pygame.K_BACKSPACE:
                        # stores text except last letter
                        j_rot = j_rot[0:-1]
                    elif len(list(j_rot)) < 3:
                        if event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            j_rot += event.unicode
                    
                
                elif box_clikt1:
                    if event.key == pygame.K_BACKSPACE:
                        
                        # stores text except last letter
                        user_text1 = user_text1[0:-1]
                    elif len(list(user_text1)) < 11:
                        if (event.unicode == "-"  and len(user_text1)==0) or (event.unicode == "." and "." not in user_text1) or event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            user_text1 += event.unicode

                elif box_clikt2:
                    if event.key == pygame.K_BACKSPACE:
                        # stores text except last letter
                        user_text2 = user_text2[0:-1]
                    elif len(list(user_text2)) < 11:
                        if (event.unicode == "-"  and len(user_text2)==0) or (event.unicode == "." and "." not in user_text2) or event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            user_text2 += event.unicode

                elif box_clikt3:
                    if event.key == pygame.K_BACKSPACE:
                        
                        # stores text except last letter
                        user_text3 = user_text3[0:-1]
                    elif len(list(user_text3)) < 11:
                        if (event.unicode == "-"  and len(user_text3)==0) or (event.unicode == "." and "." not in user_text3) or event.unicode == "1" or event.unicode == "2" or event.unicode == "3" or event.unicode == "4" or event.unicode == "5" or event.unicode == "6" or event.unicode == "7" or event.unicode == "8" or event.unicode == "9" or event.unicode == "0":
                            user_text3 += event.unicode


        if not pp:
            pp,rez_clikt = collision1(rez_clikt)
        if not pp:
            pp,j_rot_clikt = collision1(j_rot_clikt)
        if not pp:
            pp,i_rot_clikt = collision1(i_rot_clikt)
        if not pp:
            pp,box_clikt = collision1(box_clikt)
        if not pp:
            pp,box_clikt1 = collision1(box_clikt1)
        if not pp:
            pp,box_clikt2 = collision1(box_clikt2)
        if not pp:
            pp,box_clikt3 = collision1(box_clikt3)
        
        if not pp:
            pp,rez_clikt = collision2(rez_c,rez_clikt)
        if not pp:
            pp,j_rot_clikt = collision2(j_rot_c, j_rot_clikt)
        if not pp:
            pp,i_rot_clikt = collision2(i_rot_c, i_rot_clikt)
        if not pp:
            pp,box_clikt = collision2(box1, box_clikt)
        if not pp:
            pp,box_clikt1 = collision2(box2, box_clikt1)
        if not pp:
            pp,box_clikt2 = collision2(box3, box_clikt2)
        if not pp:
            pp,box_clikt3 = collision2(box4, box_clikt3)



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

        if animated:
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

        if animated:
            if user_text1 == '' or user_text1 == '-' or user_text1 == '.':
                if user_int1 < 0:
                    user_int1 += (user_int1)/20
                if user_int1 > 0:
                    user_int1 -= (user_int1)/20
            else:
                if user_int1 < float(user_text1):
                    user_int1 += (float(user_text1)-user_int1)/20
                if user_int1 > float(user_text1):
                    user_int1 -= (user_int1-float(user_text1))/20
        else:
            if user_text1 == '' or user_text1 == '-' or user_text1 == '.':
                user_int1 = 0
            else:
                user_int1 = float(user_text1)
                

        if animated:
            if user_text2 == '' or user_text2 == '-' or user_text2 == '.':
                if user_int2 < 0:
                    user_int2 += (user_int2)/20
                if user_int2 > 0:
                    user_int2 -= (user_int2)/20
            else:
                if user_int2 < float(user_text2):
                    user_int2 += (float(user_text2)-user_int2)/20
                if user_int2 > float(user_text2):
                    user_int2 -= (user_int2-float(user_text2))/20
        else:
            if user_text2 == '' or user_text2 == '-' or user_text2 == '.':
                user_int2 = 0
            else:
                user_int2 = float(user_text2)
                
        if animated:
            if user_text3 == '' or user_text3 == '-' or user_text3 == '.':
                if user_int3 < 0:
                    user_int3 += (user_int3)/20
                if user_int3 > 0:
                    user_int3 -= (user_int3)/20
            else:
                if user_int3 < float(user_text3):
                    user_int3 += (float(user_text3)-user_int3)/20
                if user_int3 > float(user_text3):
                    user_int3 -= (user_int3-float(user_text3))/20
        else:
            if user_text3 == '' or user_text3 == '-' or user_text3 == '.':
                user_int3 = 0
            else:
                user_int3 = float(user_text3)
                
        if rez == '':
            rez_t="0"
        else:
            rez_t=rez

        if i_rot == '':
            i_rot_t="0"
        else:
            i_rot_t=i_rot

        if j_rot == '':
            j_rot_t="0"
        else:
            j_rot_t=j_rot


        if animated:
            if int(i_rot_t) < i_hat_rot:
                i_hat_rot-=1
            elif int(i_rot_t) > i_hat_rot:
                i_hat_rot+=1
        else:
            if i_rot=='':
                i_hat_rot=0
            else:
                i_hat_rot=int(i_rot)


        if animated:
            if int(j_rot_t) < j_hat_rot:
                j_hat_rot-=1
            elif int(j_rot_t) > j_hat_rot:
                j_hat_rot+=1
        else:
            if j_rot=='':
                j_hat_rot=0
            else:
                j_hat_rot=int(j_rot)
        g.new_dpu(dpu)

        t_center_pos = (width // 2, height // 2)
        
        xpos=-((-(cam_vec[0]*dpu))-t_center_pos[0])
        ypos= ((-(cam_vec[1]*dpu))-t_center_pos[1])

        center_pos[0]=xpos
        center_pos[1]=-ypos

        g.resize(center_pos)

        screen.fill((255,255,255))

        g.new_rot((int(i_hat_rot),int(j_hat_rot)))
        g.add_vec_draw([2,5],[-4,1])
        g.draw_vec([4,2])

        matrix=[
            user_int,user_int1,
            user_int2,user_int3
            ]
            
        g.new_matrix(matrix)
        angle = (angle+1)%360

        g.draw_grid((int(rez_t),int(rez_t)))
        
        if 20 < pygame.mouse.get_pos()[0] < 120 and 22 < pygame.mouse.get_pos()[1] < 62:
            pygame.draw.rect(screen,[200,200,200],[20,22,100,40])
        else:
            pygame.draw.rect(screen,[150,150,150],[20,22,100,40])
        screen.blit(text , (25,27))
#my cat typed this
#wsEDXCRFzszaxdwe+
        if box_clikt:
            pygame.draw.rect(screen,[200,200,200],[box1[0][0],box1[0][1],box1[1][0]-box1[0][0],box1[1][1]-box1[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[box1[0][0],box1[0][1],box1[1][0]-box1[0][0],box1[1][1]-box1[0][1]],2)


        if box_clikt1:
            pygame.draw.rect(screen,[200,200,200],[box2[0][0],box2[0][1],box2[1][0]-box2[0][0],box2[1][1]-box2[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[box2[0][0],box2[0][1],box2[1][0]-box2[0][0],box2[1][1]-box2[0][1]],2)


        if box_clikt2:
            pygame.draw.rect(screen,[200,200,200],[box3[0][0],box3[0][1],box3[1][0]-box3[0][0],box3[1][1]-box3[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[box3[0][0],box3[0][1],box3[1][0]-box3[0][0],box3[1][1]-box3[0][1]],2)


        if box_clikt3:
            pygame.draw.rect(screen,[200,200,200],[box4[0][0],box4[0][1],box4[1][0]-box4[0][0],box4[1][1]-box4[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[box4[0][0],box4[0][1],box4[1][0]-box4[0][0],box4[1][1]-box4[0][1]],2)
        
        if rez_clikt:
            pygame.draw.rect(screen,[200,200,200],[rez_c[0][0],rez_c[0][1],rez_c[1][0]-rez_c[0][0],rez_c[1][1]-rez_c[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[rez_c[0][0],rez_c[0][1],rez_c[1][0]-rez_c[0][0],rez_c[1][1]-rez_c[0][1]],2)

        if i_rot_clikt:
            pygame.draw.rect(screen,[200,200,200],[i_rot_c[0][0],i_rot_c[0][1],i_rot_c[1][0]-i_rot_c[0][0],i_rot_c[1][1]-i_rot_c[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[i_rot_c[0][0],i_rot_c[0][1],i_rot_c[1][0]-i_rot_c[0][0],i_rot_c[1][1]-i_rot_c[0][1]],2)

        if j_rot_clikt:
            pygame.draw.rect(screen,[200,200,200],[j_rot_c[0][0],j_rot_c[0][1],j_rot_c[1][0]-j_rot_c[0][0],j_rot_c[1][1]-j_rot_c[0][1]],2)
        else:
            pygame.draw.rect(screen,[150,150,150],[j_rot_c[0][0],j_rot_c[0][1],j_rot_c[1][0]-j_rot_c[0][0],j_rot_c[1][1]-j_rot_c[0][1]],2)
        
        if animated:
            pygame.draw.rect(screen,[100,180,100],[animated_c[0][0],animated_c[0][1],animated_c[1][0]-animated_c[0][0],animated_c[1][1]-animated_c[0][1]])
        else:
            pygame.draw.rect(screen,[100,100,180],[animated_c[0][0],animated_c[0][1],animated_c[1][0]-animated_c[0][0],animated_c[1][1]-animated_c[0][1]])

        text1 = smallfont.render(user_text , True ,[0,0,0])
        text2 = smallfont.render(user_text1 , True ,[0,0,0])
        text3 = smallfont.render(user_text2 , True ,[0,0,0])
        text4 = smallfont.render(user_text3 , True ,[0,0,0])
        text5 = smallfont.render(rez , True ,[0,0,0])
        text6 = smallfont.render(i_rot , True ,[0,0,0])
        text7 = smallfont.render(j_rot , True ,[0,0,0])
        screen.blit(text1 , (23,82))
        screen.blit(text2 , (158,82))
        screen.blit(text3 , (23,142))
        screen.blit(text4 , (158,142))
        screen.blit(text5 , (23,262))
        screen.blit(text6 , (23,202))
        screen.blit(text7 , (158,202))
        pygame.display.flip()
        clock.tick(60)
        