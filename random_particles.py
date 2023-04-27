import matplotlib.pyplot as plt
import numpy as np
import math as mt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from Sim import Force_Field,particle,spring,rigid_circle,elastic_collision_handler,did_collide,calculate_elastic_collision

dr = 0.1
grid_x = 1000
grid_y = 1000
x_max = dr*(grid_x-1)
y_max = dr*(grid_y-1)
particle_num = 100
init_pos = np.random.rand(particle_num,2)*grid_x*dr
init_vel = np.random.rand(particle_num,2)*15

particles = [rigid_circle(init_pos[i],init_vel[i],1,1,x_max,y_max,1) for i in range(particle_num)]

dt = 0.01
N = 1000
path = [ [[0 for _ in range(N)], [0 for _ in range(N)]] for _ in range(particle_num)]

for i in range(N):
    print("Loading {0}%".format(100*i/N))
    elastic_collision_handler(particles)
    for j in range(particle_num):
        path[j][0][i] = particles[j].pos[0]
        path[j][1][i] = particles[j].pos[1]
        particles[j].move(dt)



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

x = [[path[i][0][j] for i in range(particle_num)] for j in range(N)]# np.arange(0, 2*np.pi, 0.01)
y = [[path[i][1][j] for i in range(particle_num)] for j in range(N)]# np.arange(0, 2*np.pi, 0.01)


line, = ax.plot(x[0], y[0],'bo')


def animate(i):

    line.set_xdata(x[i])
    line.set_ydata(y[i]) # update the data.

    return line,

print("Animating...")
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