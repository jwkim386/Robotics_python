import numpy as np

def cos(theta):
    return np.cos(theta)

def sin(theta):
    return np.sin(theta)

def hip_positions(l1, l2, phi, phi_lh, phi_rh, psi_lh, psi_rh, psi, theta, theta_lh, theta_lk, theta_rh, theta_rk, w):
    
    pos_hip_l_stance_1 = l1*(1 - cos(theta_lk))*((-(-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta))*sin(phi_lh) + sin(theta)*cos(phi_lh))*cos(theta_lh) - (-sin(psi)*sin(psi_lh)*cos(theta) + cos(psi)*cos(psi_lh)*cos(theta))*sin(theta_lh)) + l1*((-(-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta))*sin(phi_lh) + sin(theta)*cos(phi_lh))*sin(theta_lh) + (-sin(psi)*sin(psi_lh)*cos(theta) + cos(psi)*cos(psi_lh)*cos(theta))*cos(theta_lh))*sin(theta_lk) - w*(1 - cos(phi_lh))*(-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta)) + w*(1 - cos(psi_lh))*sin(psi)*cos(theta) - w*((-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta))*cos(phi_lh) + sin(phi_lh)*sin(theta)) + w*sin(phi_lh)*sin(theta) - w*sin(psi_lh)*cos(psi)*cos(theta) - (-l1 - l2)*(-((-(-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta))*sin(phi_lh) + sin(theta)*cos(phi_lh))*sin(theta_lh) + (-sin(psi)*sin(psi_lh)*cos(theta) + cos(psi)*cos(psi_lh)*cos(theta))*cos(theta_lh))*sin(theta_lk) + ((-(-sin(psi)*cos(psi_lh)*cos(theta) - sin(psi_lh)*cos(psi)*cos(theta))*sin(phi_lh) + sin(theta)*cos(phi_lh))*cos(theta_lh) - (-sin(psi)*sin(psi_lh)*cos(theta) + cos(psi)*cos(psi_lh)*cos(theta))*sin(theta_lh))*cos(theta_lk))
    pos_hip_l_stance_2 = l1*(1 - cos(theta_lk))*((-((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh))*sin(phi_lh) - sin(phi)*cos(phi_lh)*cos(theta))*cos(theta_lh) - ((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_lh))*sin(theta_lh)) + l1*((-((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh))*sin(phi_lh) - sin(phi)*cos(phi_lh)*cos(theta))*sin(theta_lh) + ((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_lh))*cos(theta_lh))*sin(theta_lk) - w*(1 - cos(phi_lh))*((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh)) - w*(1 - cos(psi_lh))*(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi)) - w*(((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh))*cos(phi_lh) - sin(phi)*sin(phi_lh)*cos(theta)) - w*(sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh) - w*sin(phi)*sin(phi_lh)*cos(theta) - (-l1 - l2)*(-((-((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh))*sin(phi_lh) - sin(phi)*cos(phi_lh)*cos(theta))*sin(theta_lh) + ((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_lh))*cos(theta_lh))*sin(theta_lk) + ((-((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_lh) - (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_lh))*sin(phi_lh) - sin(phi)*cos(phi_lh)*cos(theta))*cos(theta_lh) - ((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_lh))*sin(theta_lh))*cos(theta_lk))
    pos_hip_l_stance_3 = l1*(1 - cos(theta_lk))*((-(-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh))*sin(phi_lh) + cos(phi)*cos(phi_lh)*cos(theta))*cos(theta_lh) - ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_lh))*sin(theta_lh)) + l1*((-(-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh))*sin(phi_lh) + cos(phi)*cos(phi_lh)*cos(theta))*sin(theta_lh) + ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_lh))*cos(theta_lh))*sin(theta_lk) - w*(1 - cos(phi_lh))*(-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh)) - w*(1 - cos(psi_lh))*(sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi)) - w*((-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh))*cos(phi_lh) + sin(phi_lh)*cos(phi)*cos(theta)) - w*(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + w*sin(phi_lh)*cos(phi)*cos(theta) - (-l1 - l2)*(-((-(-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh))*sin(phi_lh) + cos(phi)*cos(phi_lh)*cos(theta))*sin(theta_lh) + ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_lh))*cos(theta_lh))*sin(theta_lk) + ((-(-(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_lh))*sin(phi_lh) + cos(phi)*cos(phi_lh)*cos(theta))*cos(theta_lh) - ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_lh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_lh))*sin(theta_lh))*cos(theta_lk))
    pos_hip_l_stance_4 = -1
    
    pos_hip_r_stance_1 = l1*(1 - cos(theta_rk))*(((-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta))*sin(phi_rh) + sin(theta)*cos(phi_rh))*cos(theta_rh) - (sin(psi)*sin(psi_rh)*cos(theta) + cos(psi)*cos(psi_rh)*cos(theta))*sin(theta_rh)) + l1*(((-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta))*sin(phi_rh) + sin(theta)*cos(phi_rh))*sin(theta_rh) + (sin(psi)*sin(psi_rh)*cos(theta) + cos(psi)*cos(psi_rh)*cos(theta))*cos(theta_rh))*sin(theta_rk) + w*(1 - cos(phi_rh))*(-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta)) - w*(1 - cos(psi_rh))*sin(psi)*cos(theta) + w*((-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta))*cos(phi_rh) - sin(phi_rh)*sin(theta)) + w*sin(phi_rh)*sin(theta) - w*sin(psi_rh)*cos(psi)*cos(theta) - (-l1 - l2)*(-(((-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta))*sin(phi_rh) + sin(theta)*cos(phi_rh))*sin(theta_rh) + (sin(psi)*sin(psi_rh)*cos(theta) + cos(psi)*cos(psi_rh)*cos(theta))*cos(theta_rh))*sin(theta_rk) + (((-sin(psi)*cos(psi_rh)*cos(theta) + sin(psi_rh)*cos(psi)*cos(theta))*sin(phi_rh) + sin(theta)*cos(phi_rh))*cos(theta_rh) - (sin(psi)*sin(psi_rh)*cos(theta) + cos(psi)*cos(psi_rh)*cos(theta))*sin(theta_rh))*cos(theta_rk))
    pos_hip_r_stance_2 = l1*(1 - cos(theta_rk))*((((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh))*sin(phi_rh) - sin(phi)*cos(phi_rh)*cos(theta))*cos(theta_rh) - (-(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_rh))*sin(theta_rh)) + l1*((((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh))*sin(phi_rh) - sin(phi)*cos(phi_rh)*cos(theta))*sin(theta_rh) + (-(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_rh))*cos(theta_rh))*sin(theta_rk) + w*(1 - cos(phi_rh))*((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh)) + w*(1 - cos(psi_rh))*(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi)) + w*(((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh))*cos(phi_rh) + sin(phi)*sin(phi_rh)*cos(theta)) - w*(sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh) - w*sin(phi)*sin(phi_rh)*cos(theta) - (-l1 - l2)*(-((((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh))*sin(phi_rh) - sin(phi)*cos(phi_rh)*cos(theta))*sin(theta_rh) + (-(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_rh))*cos(theta_rh))*sin(theta_rk) + ((((-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*cos(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*sin(psi_rh))*sin(phi_rh) - sin(phi)*cos(phi_rh)*cos(theta))*cos(theta_rh) - (-(-sin(phi)*sin(psi)*sin(theta) + cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*sin(theta)*cos(psi) + sin(psi)*cos(phi))*cos(psi_rh))*sin(theta_rh))*cos(theta_rk))
    pos_hip_r_stance_3 = l1*(1 - cos(theta_rk))*((((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh))*sin(phi_rh) + cos(phi)*cos(phi_rh)*cos(theta))*cos(theta_rh) - ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_rh) - (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_rh))*sin(theta_rh)) + l1*((((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh))*sin(phi_rh) + cos(phi)*cos(phi_rh)*cos(theta))*sin(theta_rh) + ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_rh) - (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_rh))*cos(theta_rh))*sin(theta_rk) + w*(1 - cos(phi_rh))*((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh)) + w*(1 - cos(psi_rh))*(sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi)) + w*(((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh))*cos(phi_rh) - sin(phi_rh)*cos(phi)*cos(theta)) - w*(sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + w*sin(phi_rh)*cos(phi)*cos(theta) - (-l1 - l2)*(-((((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh))*sin(phi_rh) + cos(phi)*cos(phi_rh)*cos(theta))*sin(theta_rh) + ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_rh) - (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_rh))*cos(theta_rh))*sin(theta_rk) + ((((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*sin(psi_rh) + (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*cos(psi_rh))*sin(phi_rh) + cos(phi)*cos(phi_rh)*cos(theta))*cos(theta_rh) - ((sin(phi)*sin(psi) - sin(theta)*cos(phi)*cos(psi))*cos(psi_rh) - (sin(phi)*cos(psi) + sin(psi)*sin(theta)*cos(phi))*sin(psi_rh))*sin(theta_rh))*cos(theta_rk))
    pos_hip_r_stance_4 = -1
    
    pos_hip_l_stance = np.array([pos_hip_l_stance_1, pos_hip_l_stance_2, pos_hip_l_stance_3, pos_hip_l_stance_4])
    pos_hip_r_stance = np.array([pos_hip_r_stance_1, pos_hip_r_stance_2, pos_hip_r_stance_3, pos_hip_r_stance_4])
    
    return pos_hip_l_stance, pos_hip_r_stance
