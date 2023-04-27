import matplotlib.pyplot as plt
import numpy as np
import math as mt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

G=6.67430*10**(-11) # Universal Gravity constant

class Force_Field:
    F = []
    x = 0
    y = 0

    def __init__(self, Fx, Fy, x_grid, y_grid):
        self.x = x_grid
        self.y = y_grid
        self.F = np.zeros((2, self.x, self.y), dtype=float)
        self.F[0] = Fx
        self.F[1] = Fy


class particle:
    pos = np.array([0, 0], dtype=float)
    vel = np.array([0, 0], dtype=float)
    Force = np.array([0, 0], dtype=float)
    x = 999999
    y = 999999
    mass = 0
    loss =1
    def __init__(self, init_pos, init_vel, m, xmax, ymax,collision_loss=1.0):
        self.pos = np.array(init_pos)
        self.vel = np.array(init_vel)
        self.mass = m
        self.x = xmax
        self.y = ymax
        self.loss = collision_loss

    def move(self, dt):
        self.vel = self.vel + np.multiply(self.Force, (dt / self.mass))
        self.pos = self.pos + self.vel * dt
        if (self.pos[0] > self.x):
            self.pos[0] = self.x
            self.vel[0] = -self.loss*self.vel[0]
        elif(self.pos[0]<0):
            self.pos[0] = 0
            self.vel[0] = -self.loss*self.vel[0]
        if self.pos[1] > self.y:
            self.pos[1] = self.y
            self.vel[1] = -self.loss*self.vel[1]
        elif(self.pos[1]<0):
            self.pos[1] = 0
            self.vel[1] = -self.loss*self.vel[1]

    def update_F(self, F):
        self.Force = F
#elastic
class rigid_circle(particle):
    pos = np.array([0, 0], dtype=float)
    vel = np.array([0, 0], dtype=float)
    Force = np.array([0, 0], dtype=float)
    x = 999999
    y = 999999
    mass = 0
    r= 0
    def __init__(self, init_pos, init_vel, m,radius, xmax, ymax,loss):
        particle.__init__(self,init_pos,init_vel,m,xmax,ymax,loss)
        self.r = radius


def Gravity_Field_Generator(G_pos,G,dr,grid_x,grid_y):

    Fx = np.zeros((grid_x, grid_y), dtype=float)
    Fy = np.zeros((grid_x, grid_y), dtype=float)

    for i in range(grid_x):
        for j in range(grid_y):
            r = dr * (np.array([i, j]) - G_pos)
            Fx[i][j] = -r[0] * G / np.power(np.linalg.norm(r), 3)
            Fy[i][j] = -r[1] * G / np.power(np.linalg.norm(r), 3)

    return Fx,Fy

class Gravity_Source:
    def Calc_F(self,particl_arr):

        return None


class spring:
    pos = np.zeros((2,1))
    k = 0
    beta = 0
    l = 0
    def __init__(self,pos,spring_const,damp_const,stable_len=0):
        self.pos = pos
        self.k=spring_const
        self.beta = damp_const
        self.l = stable_len
    def calc_force(self,p_pos,p_vel):
        #print("Spring: {0}, damp: {1}".format(self.k*(self.pos-p_pos),self.beta*p_vel))
        r = self.pos-p_pos
        l_v = self.l*r/np.linalg.norm(r)

        return self.k*(r-l_v)-self.beta*p_vel



def did_collide(body1,body2):
    return np.linalg.norm( body1.pos-body2.pos)<=(body1.r+body2.r)
#elastic
#https://courses.lumenlearning.com/boundless-physics/chapter/collisions/#:~:text=v%202%20i%20.-,If%20two%20particles%20are%20involved%20in%20an%20elastic%20collision%2C%20the,m%201%20)%20v%202%20i%20.
def calculate_elastic_collision(body1,body2):
    m1 = body1.mass
    m2 = body2.mass
    v1 = np.copy(body1.vel)
    v2 = np.copy(body2.vel)
    body2.vel = ((2*m1)/(m1+m2))*v1+(m2-m1)/(m1+m2)*v2
    body1.vel =body2.vel+v2-v1


def elastic_collision_handler(body_list):
    for i in range(len(body_list)):
        for j in range(i,len(body_list)):
            if did_collide(body_list[i],body_list[j]):
                calculate_elastic_collision(body_list[i],body_list[j])