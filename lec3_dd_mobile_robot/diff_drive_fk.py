from matplotlib import pyplot as plt
# from scipy.optimize import fsolve
import math
import numpy as np

def animate(t,z):
    R = 0.1;
    
    for i in range(0,len(t)):
        x, y, theta = z[i]

        x2 = x + R*np.cos(theta)
        y2 = y + R*np.sin(theta)

        robot,  = plt.plot(x,y,color='green',marker = 'o',markersize=15)
        line, = plt.plot([x, x2],[y, y2],color="black")
        shape, = plt.plot(z[0:i,0],z[0:i,1],color='red');

        plt.xlim(-2,2)
        plt.ylim(-2,2)
        plt.gca().set_aspect('equal')
        plt.pause(0.1)
        line.remove()
        robot.remove()
        shape.remove()

def euler_integration(tspan,z0,u):
    v, omega = u
    h = tspan[1] - tspan[0]
    x0, y0, theta0 = z0
    
    xdot_c = v*math.cos(theta0)
    ydot_c = v*math.sin(theta0)
    thetadot = omega

    x1 = x0 + xdot_c * h
    y1 = y0 + ydot_c * h
    theta1 = theta0 + thetadot * h

    return [x1, y1, theta1]

#initial condition, [x0, y0, theta0]
z0 = [0, 0, -math.pi/2]

#integration time step
h = 0.1

# %%%%% the controls are v = speed and omega = direction
# %%%%%% v = 0.5r(phidot_r + phidot_l)
# %%%%%% omega = 0.5 (r/b)*(phitdot_r - phidot_l)
# %%%%%% these are set below %%%%%%
# %%%%%%% writing letters %%%%%%%
t1 = np.arange(0,1,0.1)
t2 = np.arange(1,2,0.1)
t3 = np.arange(2,3,0.1)
t = np.append(t1,t2)
t = np.append(t,t3)
u = np.zeros((len(t), 2))
for i in range(0,len(t1)):
    u[i,0] = 1
for i in range(len(t1),len(t1)+len(t1)):
    u[i,1] = math.pi/2
    u[i,0] = 1
for i in range(len(t1)+len(t2),len(t)):
    u[i,0] = 1

z = np.array(z0);
for i in range(0,len(t)-1):
    # u = [0.5, 0] #[v, omega] #test
    z0 = euler_integration([t[i], t[i+1]],z0,[u[i,0],u[i,1]])
    z = np.vstack([z, z0])

animate(t,z)
  
if __name__=="__main__":
    try:
        draw_2d_mpl(circle=False)
    except Exception as e:
        print(e)
    finally:
        plt.close()
