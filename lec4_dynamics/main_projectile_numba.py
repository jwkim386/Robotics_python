from matplotlib import pyplot as plt
import numpy as np
import math

from numba import jit
from scipy import interpolate
from scipy.integrate import odeint

class parameters:
    def __init__(self):
        self.g = 9.81
        self.m = 1
        self.c = 0.47
        self.pause = 0.01
        self.fps = 10
        self.t_length = 5

def interpolation(t, z, params):

    #interpolation
    t_interp = np.arange(t[0], t[len(t)-1], 1/params.fps)
    [rows, cols] = np.shape(z)
    z_interp = np.zeros((len(t_interp), cols))

    for i in range(0, cols):
        f = interpolate.interp1d(t, z[:,i])
        z_interp[:,i] = f(t_interp)

    return t_interp, z_interp

def animate(t_interp,z_interp,parms):
    #plot
    for i in range(0,len(t_interp)):
        traj, = plt.plot(z_interp[0:i,0],z_interp[0:i,2],color='red');
        prj, =  plt.plot(z_interp[i,0],z_interp[i,2],color='red',marker='o');

        plt.xlim(min(z[:,0]-1),max(z[:,0]+1))
        plt.ylim(min(z[:,2]-1),max(z[:,2]+1))
        # plt.gca().set_aspect('equal')
        plt.pause(parms.pause)
        traj.remove()
        prj.remove()

    # plt.close()
    fig2, (ax, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1)

    ax.set_title("X")
    ax.plot(t_interp, z_interp[:,0], color="green")

    ax2.set_title("X dot")
    ax2.plot(t_interp, z_interp[:,1], color="orange")

    ax3.set_title("Y")
    ax3.plot(t_interp, z_interp[:,2], color="green")

    ax4.set_title("Y dot")
    ax4.plot(t_interp, z_interp[:,3], color="orange")

    plt.show()

def projectile(z, t, m,g,c):

    x, xdot, y, ydot = z
    v = np.sqrt(xdot**2+ydot**2)

    #%%%% drag is prop to v^2
    dragX = c * v * xdot
    dragY = c * v * ydot

    #%%%% net acceleration %%%
    ax =  0 - (dragX / m) #xddot
    ay = -g - (dragY / m) #yddot

    return np.array([xdot, ax, ydot, ay])

def simulation():
    params = parameters()
    # initial state
    x0, x0dot, y0, y0dot = (0, 100, 0, 100*math.tan(math.pi/3))
    z0 = np.array([x0, x0dot, y0, y0dot])

    t_start, t_end = (0, params.t_length)
    t = np.arange(t_start, t_end, 0.01)

    try:
        # calc states from ode solved
        
        # # # case1. ordinary odeint => 0.0031407199999999857
        # z = odeint(projectile, z0, t, args=(params.m,params.g,params.c)
        #            ,rtol=1e-3,atol=1e-6)
        
        # case2. odeint with numba => 0.22621529699999998
        projectile_numba = jit(projectile,nopython=True)
        z = odeint(projectile_numba, z0, t, args=(params.m,params.g,params.c),
                   rtol=1e-3,atol=1e-6)
    except Exception as e:
        print(e)
    finally:
        # interpolation for ploting
        # t_interp, z_interp = interpolation(t, z, params)
        # Draw plot
        # animate(t_interp,z_interp,params)
        print("Everything done!")


if __name__=="__main__":
    
    import timeit

    result = timeit.Timer(simulation).timeit(number=1)
    
    print(result)