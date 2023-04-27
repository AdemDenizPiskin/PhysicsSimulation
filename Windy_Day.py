import matplotlib.pyplot as plt
import numpy as np
import math as mt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from Sim import Force_Field,particle

dr = 0.1
grid_x = 1000
grid_y = 1000
g = 9.81
x_0 = np.array([0,50])
v_0 = 0*np.array([12,16])
m1 = 5
xmax = (grid_x-1)*dr
ymax = (grid_y-1)*dr
particle1 = particle(x_0,v_0,m1,xmax,ymax)
#particle2 = particle([50,50],[0,0],3,99.9,99.9)
dt = 0.01
N = 10000
path1 = [[0 for _ in range(N)], [0 for _ in range(N)]]
wind1 = [[0,0] for _ in range(N)]
#path2 = [[0 for _ in range(N)], [0 for _ in range(N)]]
for i in range(N):
    path1[0][i] = particle1.pos[0]
    path1[1][i] = particle1.pos[1]
    #path2[0][i] = particle2.pos[0]
    #path2[1][i] = particle2.pos[1]
    rng = np.random.randint(-50,50,size=2)
    F_wind = 2*m1*(3*np.ones(2)+rng/35)
    wind1[i] = F_wind
    particle1.update_F(np.array([0,-particle1.mass*g])+F_wind)
    #elastic_collision_handler([particle1,particle2])
    particle1.move(dt)
    #particle2.move(dt)

t = [i * dt for i in range(N)]
'''
plt.figure(1)
plt.plot(path[0], path[1])

plt.figure(2)
plt.plot(t, velocity[0])
plt.figure(3)
plt.plot(t, velocity[1])

plt.figure(4)
plt.plot(t, acc[0])
plt.figure(5)
plt.plot(t, acc[1])
'''
'''
plt.figure(1)
plt.quiver(path[0], path[1], velocity[0], velocity[1],color='r')
plt.plot(50,50,'bo')

plt.figure(2)
plt.quiver(path[0], path[1], acc[0], acc[1],color='g')
plt.plot(50,50,'bo')

plt.show()
'''


fig, ax = plt.subplots()

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

x1 = path1[0]# np.arange(0, 2*np.pi, 0.01)
y1 = path1[1]
#x2 = path2[0]
#y2 = path2[1]
line, = ax.plot(x1[0], y1[0],'b', marker='o', linestyle='dashed')
#line2, = ax.plot(x2[0], y2[0],'r', marker='o', linestyle='dashed')

field = ax.quiver(50,50,wind1[0][0],wind1[0][1])


def animate(i):

    line.set_xdata(x1[i])
    line.set_ydata(y1[i]) # update the data.
    #line2.set_xdata(x2[i])
    #line2.set_ydata(y2[i])
    #

    field.set_UVC(wind1[i][0],wind1[i][1])
    return line,field


ani = FuncAnimation(
    fig, animate, interval=0, frames=np.arange(1,N))

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()