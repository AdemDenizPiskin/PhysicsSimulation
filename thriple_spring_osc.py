import matplotlib.pyplot as plt
import numpy as np
import math as mt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from Sim import Force_Field,particle,spring,rigid_circle

dr = 0.1
grid_x = 1000
grid_y = 1000
x_max = (grid_x-1)*dr
y_max = (grid_y-1)*dr
a = 10
r1 = np.array([a,a*np.sqrt(3)]) + np.array([50,50])+np.random.randint(-49,50,size=2)/10
r2 = np.array([-a,a*np.sqrt(3)])+ np.array([50,50])+np.random.randint(-49,50,size=2)/10
r3 = np.array([0,-2*a])+ np.array([50,50]) + np.random.randint(-49,50,size=2)/10

v1 = np.random.randint(-49,50,size=2)/30
v2= np.random.randint(-49,50,size=2)/30
v3= np.random.randint(-49,50,size=2)/30
#Fx,Fy = Gravity_source(G_pos,G,dr,grid_x,grid_y)
k = 3
gamma = 0.1
#Test_F = Force_Field(Fx, Fy, grid_x, grid_y)
particle1 = particle(r1,v1, 1, 99.9, 99.9)
particle2 = particle(r2,v2, 1, 99.9, 99.9)
particle3 = particle(r3,v3, 16, 99.9, 99.9)

spring12_pos = particle1.pos
spring23_pos = particle2.pos
spring31_pos = particle3.pos

spring12 = spring(spring12_pos*dr,k,gamma,2*a)
spring23 = spring(spring23_pos*dr,k,gamma,2*a)
spring31 = spring(spring31_pos*dr,k,gamma,2*a)
dt = 0.01
N = 10000
path1 = [[0 for _ in range(N)], [0 for _ in range(N)]]
path2 = [[0 for _ in range(N)], [0 for _ in range(N)]]
path3 = [[0 for _ in range(N)], [0 for _ in range(N)]]

for i in range(N):
    path1[0][i] = particle1.pos[0]
    path1[1][i] = particle1.pos[1]
    path2[0][i] = particle2.pos[0]
    path2[1][i] = particle2.pos[1]
    path3[0][i] = particle3.pos[0]
    path3[1][i] = particle3.pos[1]

    spring12.pos = particle1.pos
    spring23.pos = particle2.pos
    spring31.pos = particle3.pos
    F12 = spring12.calc_force(particle2.pos,particle2.vel)
    F23 = spring23.calc_force(particle3.pos, particle3.vel)
    F31 =  spring31.calc_force(particle1.pos, particle1.vel)
    particle1.update_F(F31-F12)
    particle2.update_F(F12-F23)
    particle3.update_F(F23-F31)
    #print(int(test_particle.pos[0] / dr),int(test_particle.pos[1] / dr))
    #test_particle.update_F(np.array([Test_F.F[0][int(test_particle.pos[0] / dr)][int(test_particle.pos[1] / dr)],
    #                                 Test_F.F[1][int(test_particle.pos[0] / dr)][int(test_particle.pos[1] / dr)]]))
    particle1.move(dt)
    particle2.move(dt)
    particle3.move(dt)

t = [i * dt for i in range(N)]

fig, ax = plt.subplots()

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

x1 = path1[0]# np.arange(0, 2*np.pi, 0.01)
y1 = path1[1]
x2 = path2[0]# np.arange(0, 2*np.pi, 0.01)
y2 = path2[1]
x3 = path3[0]# np.arange(0, 2*np.pi, 0.01)
y3 = path3[1]
line, = ax.plot(x1[0],y1[0],'b', marker='o')
line2, = ax.plot(x2[0],y2[0],'bo')
line3, = ax.plot(x3[0],y3[0],'ro')
line4, = ax.plot([x1[0],x2[0],x3[0],x1[0]],[y1[0], y2[0], y3[0],y1[0]],'--m', )

def animate(i):

    line.set_xdata(x1[i])
    line.set_ydata(y1[i]) # update the data.
    line2.set_xdata(x2[i])
    line2.set_ydata(y2[i])
    line3.set_xdata(x3[i])
    line3.set_ydata(y3[i])
    line4.set_xdata([x1[i],x2[i],x3[i],x1[i]])
    line4.set_ydata([y1[i], y2[i], y3[i],y1[i]])
    return line,line2,line3,


ani = FuncAnimation(
    fig, animate, interval=0, frames=np.arange(1,N))


plt.show()