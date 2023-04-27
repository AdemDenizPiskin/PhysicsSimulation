import matplotlib.pyplot as plt
import numpy as np
import math as mt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from Sim import Force_Field,particle,Gravity_Field_Generator,spring

dr = 0.1
grid_x = 1000
grid_y = 1000
G = 12.98
G_pos = np.array([500, 500])
spring1_pos = np.array([1000,1000])
spring2_pos = np.array([0,0])
Fx,Fy = Gravity_Field_Generator(G_pos,G,dr,grid_x,grid_y)

Test_F = Force_Field(Fx, Fy, grid_x, grid_y)
test_particle = particle(np.array([450 * dr, 500 * dr]),np.array( [0, 1]), 1, 99.9, 99.9)
spring1 = spring(spring1_pos*dr,1.0,0.2,2)
spring2 = spring(spring2_pos*dr,1.0,0.2,2)

dt = 0.01
N = 10000
path = [[0 for _ in range(N)], [0 for _ in range(N)]]
velocity = [[0 for _ in range(N)], [0 for _ in range(N)]]
acc = [[0 for _ in range(N)], [0 for _ in range(N)]]
for i in range(N):
    path[0][i] = test_particle.pos[0]
    path[1][i] = test_particle.pos[1]
    velocity[0][i] = test_particle.vel[0]
    velocity[1][i] = test_particle.vel[1]
    acc[0][i] = test_particle.Force[0] / test_particle.mass
    acc[1][i] = test_particle.Force[1] / test_particle.mass
    #print(int(test_particle.pos[0] / dr),int(test_particle.pos[1] / dr))
    test_particle.update_F(np.array([Test_F.F[0][int(test_particle.pos[0] / dr)][int(test_particle.pos[1] / dr)],
                                     Test_F.F[1][int(test_particle.pos[0] / dr)][int(test_particle.pos[1] / dr)]]))
    #test_particle.update_F(spring1.calc_force(test_particle.pos,test_particle.vel)+spring2.calc_force(test_particle.pos,test_particle.vel))
    test_particle.move(dt)

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

ax.set_xlim(40, 60)
ax.set_ylim(40, 60)

x = path[0]# np.arange(0, 2*np.pi, 0.01)
y = path[1]
line, = ax.plot(x[0], y[0],'b', marker='o', linestyle='dashed')
line2, = ax.plot(G_pos[0]*dr,G_pos[1]*dr,'ro')


def animate(i):

    line.set_xdata(x[i])

    line.set_ydata(y[i]) # update the data.
    return line,


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