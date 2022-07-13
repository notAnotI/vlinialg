import math
import pygame

class graph:
    def __init__(self,disp,dpu=40,matrix=[1,0,0,1],size=(400,400),rot=(45,0)):
        # asining variables
        self.disp,self.matrix,self.dpu,self.size,self.rot,self.t_matrix = disp,matrix,dpu,size,rot,matrix
        self.new_rot(self.rot)
    
    def new_matrix(self,matrix):
        # reasining variable matrix
        self.t_matrix = matrix

    def new_dpu(self,dpu):
        # reasining variable 
        self.dpu = dpu

    def new_rot(self,rot):
        # reasining variable 
        self.rot = rot
        i_hat = self.rotate(self.rot[0],self.t_matrix[0],self.t_matrix[2])
        j_hat = self.rotate(self.rot[1],self.t_matrix[1],self.t_matrix[3])
        self.matrix=[i_hat[0],j_hat[0],i_hat[1],j_hat[1]]

    def rotate(self, angle, x, y):
        # this function is used to rotate a point around (0,0)
        rx=x
        ry=y
        rad = angle * math.pi / 180 # math shit
        cosa = math.cos(rad)         # more math shit
        sina = math.sin(rad)          # even more math shit
        x = rx * cosa - ry * sina     # stil more
        y = rx * sina + ry * cosa     # almost done
        return  (x,y)                     # finely

    def draw_vec(self,vec=[0,3],bol=True,c=(0,0,0)):
        x=(round((vec[0]*self.matrix[0])*self.dpu)+round((vec[1]*self.matrix[1])*self.dpu))+self.size[0]      # converding vector to cords on screen
        y=(round((-vec[0]*self.matrix[2])*self.dpu)+round((-vec[1]*self.matrix[3])*self.dpu))+self.size[1]   # same here
        try:
            if bol:
                pygame.draw.line(self.disp,c,(self.size[0],self.size[1]),(x,y))  #drawing line from (0,0) to the cords
        except TypeError:
            pass
        return (x,y)

    def add_vec_draw(self,vec1=[1,2],vec2=[2,1],c1=((100,100,200)),c2=(200,100,100),c3=((100,200,100))):
        x=(round((vec1[0]*self.matrix[0])*self.dpu)+round((vec1[1]*self.matrix[1])*self.dpu))+self.size[0]
        y=(round((-vec1[0]*self.matrix[2])*self.dpu)+round((-vec1[1]*self.matrix[3])*self.dpu))+self.size[1]
        try:
            pygame.draw.line(self.disp,c1,(self.size[0],self.size[1]),(x,y))
        except TypeError:
            pass
        xx=x
        yy=y
        x=(round((vec2[0]*self.matrix[0])*self.dpu)+round((vec2[1]*self.matrix[1])*self.dpu))+xx
        y=(round((-vec2[0]*self.matrix[2])*self.dpu)+round((-vec2[1]*self.matrix[3])*self.dpu))+yy
        try:
            pygame.draw.line(self.disp,c2,(xx,yy),(x,y))
            pygame.draw.line(self.disp,c3,(self.size[0],self.size[1]),(x,y))
        except TypeError:
            pass
        return (x,y)
    
    def add_vec_draw2(self,vec1=[1,2],vec2=[2,1],c2=(100,100,200)):
        x=(round((vec1[0]*self.matrix[0])*self.dpu)+round((vec1[1]*self.matrix[1])*self.dpu))+self.size[0]
        y=(round((-vec1[0]*self.matrix[2])*self.dpu)+round((-vec1[1]*self.matrix[3])*self.dpu))+self.size[1]
        xx=x
        yy=y
        x=(round((vec2[0]*self.matrix[0])*self.dpu)+round((vec2[1]*self.matrix[1])*self.dpu))+xx
        y=(round((-vec2[0]*self.matrix[2])*self.dpu)+round((-vec2[1]*self.matrix[3])*self.dpu))+yy
        try:
            pygame.draw.line(self.disp,c2,(xx,yy),(x,y))
        except TypeError:
            pass
        return (x,y)
    
    def resize(self,size):
        self.size = size


    def draw_grid(self,rez=(15,15)):
        for y in range(-rez[1],rez[1]):
            for x in range(-rez[0],rez[0]):
                xy=((round((x*self.matrix[0])*self.dpu)+round((y*self.matrix[1])*self.dpu))+self.size[0],(round((-x*self.matrix[2])*self.dpu)+round((-y*self.matrix[3])*self.dpu))+self.size[1])
                try:
                    try:
                        pygame.draw.line(self.disp,(100,100,200),yx,xy)
                    except UnboundLocalError:
                        pass
                except TypeError:
                    pass
                yx=xy
            del yx

        for x in range(-rez[0],rez[0]):
            for y in range(-rez[1],rez[1]):
                xy=((round((x*self.matrix[0])*self.dpu)+round((y*self.matrix[1])*self.dpu))+self.size[0],(round((-x*self.matrix[2])*self.dpu)+round((-y*self.matrix[3])*self.dpu))+self.size[1])
                try:
                    try:
                        pygame.draw.line(self.disp,(100,100,200),yx,xy)
                    except UnboundLocalError:
                        pass
                except TypeError:
                    pass
                yx=xy
            del yx
        self.draw_vec([rez[0]-1,0],(200,100,100))
        self.draw_vec([-rez[0],0],(200,100,100))
        self.draw_vec([0,rez[1]-1],(100,200,100))
        self.draw_vec([0,-rez[1]],(100,200,100))     

    def bird(self,rez=(15,15)):
        for x in range(-rez[0],rez[0]):
            self.draw_vec2([x,rez[1]],[x,-rez[1]])
        for y in range(-rez[1],rez[1]):
            self.draw_vec2([rez[0],y],[-rez[0],y])

    def draw_grid2(self,rez=(15,15)):
        for y in range(-rez[1],rez[1]+1):
            if y != 0:
                self.add_vec_draw2([-rez[0],y],[rez[0],0])
                self.add_vec_draw2([rez[0],y],[-rez[0],0])
        for x in range(-rez[0],rez[0]+1):
            if x != 0:
                self.add_vec_draw2([x,-rez[0]],[0,rez[0]])
                self.add_vec_draw2([x,rez[0]],[0,-rez[0]])
        self.draw_vec([rez[0],0],True,(200,100,100))
        self.draw_vec([-rez[0],0],True,(200,100,100))
        self.draw_vec([0,rez[1]],True,(100,200,100))
        self.draw_vec([0,-rez[1]],True,(100,200,100))    

