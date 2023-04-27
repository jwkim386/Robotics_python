from matplotlib import pyplot as plt
import numpy as np
import math
from scipy import interpolate
from scipy.integrate import odeint

class parameters:
    def __init__(self):
        self.m1 = 1
        self.m2 = 1
        self.I1 = 0.1
        self.I2 = 0.1
        self.c1 = 0.5
        self.c2 = 0.5
        self.l = 1
        self.g = 9.81
        self.pause = 0.02
        self.fps = 20

def cos(angle):
    return np.cos(angle)

def sin(angle):
    return np.sin(angle);

def interpolation(t, z, params):

    #interpolation
    t_interp = np.arange(t[0], t[len(t)-1], 1/params.fps)
    [rows, cols] = np.shape(z)
    z_interp = np.zeros((len(t_interp), cols))

    for i in range(0, cols):
        f = interpolate.interp1d(t, z[:,i])
        z_interp[:,i] = f(t_interp)

    return t_interp, z_interp

def animate(t_interp, z_interp, params):

    l = params.l
    c1 = params.c1
    c2 = params.c2

    # #plot
    for i in range(0,len(t_interp)):
        theta1 = z_interp[i,0];
        theta2 = z_interp[i,2];
        O = np.array([0, 0])
        P = np.array([l*sin(theta1), -l*cos(theta1)])
        # 그림을 그려야 하니까 + P를 해주었음
        Q = P + np.array([l*sin(theta1+theta2),-l*cos(theta1+theta2)])
        
        # 사실 이렇게도 구할 수 있다.
        # H_01 = np.array([
        #     [np.cos(3*np.pi/2 + theta1), -np.sin(3*np.pi/2 + theta1), 0],
        #     [np.sin(3*np.pi/2 + theta1), -np.cos(3*np.pi/2 + theta1), 0],
        #     [0, 0, 1],
        # ])
        # H_12 = np.array([
        #     [np.cos(theta2), -np.sin(theta2), 0],
        #     [np.sin(theta2), -np.cos(theta2), 0],
        #     [0, 0, 1],
        # ])

        # COM Point
        G1 = np.array([c1*sin(theta1), -c1*cos(theta1)])
        G2 = P + np.array([c2*sin(theta1+theta2),-c2*cos(theta1+theta2)])

        pend1, = plt.plot([O[0], P[0]],[O[1], P[1]],linewidth=5, color='red')
        pend2, = plt.plot([P[0], Q[0]],[P[1], Q[1]],linewidth=5, color='blue')
        com1, = plt.plot(G1[0],G1[1],color='black',marker='o',markersize=10)
        com2, = plt.plot(G2[0],G2[1],color='black',marker='o',markersize=10)

        plt.xlim(-2,2)
        plt.ylim(-2,2)
        plt.gca().set_aspect('equal')

        plt.pause(params.pause)

        if (i < len(t_interp)-1):
            pend1.remove()
            pend2.remove()
            com1.remove()
            com2.remove()

    #plt.show()
    plt.show(block=False)
    plt.pause(1)
    plt.close()

    # result plotting
    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.plot(t,z[:,0],color='red',label='theta1');
    plt.plot(t,z[:,2],color='blue',label='theta2');
    plt.ylabel("angle")
    plt.legend(loc="upper left")
    
    plt.subplot(2, 1, 2)
    plt.plot(t,z[:,1],color='red',label='omega1');
    plt.plot(t,z[:,3],color='blue',label='omega2');
    plt.xlabel("t")
    plt.ylabel("angular rate")
    plt.legend(loc="lower left")

    plt.show()

def double_pendulum(z0, t, m1, m2, I1, I2, c1, c2, link1, g):
    
    theta1, omega1, theta2, omega2 = z0

    M11 =  1.0*I1 + 1.0*I2 + c1**2*m1 + m2*(c2**2 + 2*c2*link1*cos(theta2) + link1**2)
    M12 =  1.0*I2 + c2*m2*(c2 + link1*cos(theta2))
    M21 =  1.0*I2 + c2*m2*(c2 + link1*cos(theta2))
    M22 =  1.0*I2 + c2**2*m2 

    C1 =  -c2*link1*m2*omega2*(2.0*omega1 + 1.0*omega2)*sin(theta2)
    C2 =  c2*link1*m2*omega1**2*sin(theta2) 

    G1 =  g*(c1*m1*sin(theta1) + m2*(c2*sin(theta1 + theta2) + link1*sin(theta1)))
    G2 =  c2*g*m2*sin(theta1 + theta2)

    A = np.array([
        [M11, M12],
        [M21, M22],
    ])
    b = -1 * np.array([ C1 + G1, C2 + G2 ])

    x = np.linalg.inv(A) @ b
    
    return [omega1, x[0], omega2, x[1]]

if __name__=="__main__":

    params = parameters()

    t = np.linspace(0, 10, 500)
    
    # initlal state
    z0 = np.array([np.pi, 0.001, 0, 0])
    all_params = (
        params.m1, params.m2,
        params.I1, params.I2,
        params.c1, params.c2,
        params.l,  params.g
    )
    z = odeint(double_pendulum, z0, t, args=all_params)
    t_interp, z_interp = interpolation(t, z, params)

    animate(t_interp, z_interp, params)