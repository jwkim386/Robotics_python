import numpy as np 
from libc.math cimport sin, cos

cimport numpy as cnp
cnp.import_array()

DTYPE = np.float64
ctypedef cnp.float64_t DTYPE_t

# z: size 6 ndarray
# params: size 13 ndarray

cimport cython
@cython.boundscheck(False)
@cython.wraparound(False)
def nlink_rhs(cnp.ndarray[DTYPE_t, ndim=1] z, cnp.ndarray[DTYPE_t, ndim=1] params): 

    cdef float q_0 = z[0]
    cdef float u_0 = z[1]
    cdef float q_1 = z[2]
    cdef float u_1 = z[3]
    cdef float q_2 = z[4]
    cdef float u_2 = z[5]
    
    cdef float m_0 = params[0]
    cdef float I_0 = params[1]
    cdef float c_0 = params[2]
    cdef float l_0 = params[3]
    cdef float m_1 = params[4]
    cdef float I_1 = params[5]
    cdef float c_1 = params[6]
    cdef float l_1 = params[7]
    cdef float m_2 = params[8]
    cdef float I_2 = params[9]
    cdef float c_2 = params[10]
    cdef float l_2 = params[11]
    cdef float g = params[12]

    cdef cnp.ndarray M = np.zeros([3, 3], dtype=DTYPE)
    cdef cnp.ndarray C = np.zeros([3, 1], dtype=DTYPE)
    cdef cnp.ndarray G = np.zeros([3, 1], dtype=DTYPE)

    M00 = 1.0*I_0 + 1.0*I_1 + 1.0*I_2 + c_0**2*m_0 + m_1*(c_1**2 + 2*c_1*l_0*cos(q_1) + l_0**2) + m_2*(c_2**2 + 2*c_2*l_0*cos(q_1 + q_2) + 2*c_2*l_1*cos(q_2) + l_0**2 + 2*l_0*l_1*cos(q_1) + l_1**2) 
    M01 = 1.0*I_1 + 1.0*I_2 + c_1*m_1*(c_1 + l_0*cos(q_1)) + m_2*(c_2**2 + c_2*l_0*cos(q_1 + q_2) + 2*c_2*l_1*cos(q_2) + l_0*l_1*cos(q_1) + l_1**2) 
    M02 = 1.0*I_2 + c_2*m_2*(c_2 + l_0*cos(q_1 + q_2) + l_1*cos(q_2)) 
    M10 = 1.0*I_1 + 1.0*I_2 + c_1*m_1*(c_1 + l_0*cos(q_1)) + m_2*(c_2**2 + c_2*l_0*cos(q_1 + q_2) + 2*c_2*l_1*cos(q_2) + l_0*l_1*cos(q_1) + l_1**2) 
    M11 = 1.0*I_1 + 1.0*I_2 + c_1**2*m_1 + m_2*(c_2**2 + 2*c_2*l_1*cos(q_2) + l_1**2) 
    M12 = 1.0*I_2 + c_2*m_2*(c_2 + l_1*cos(q_2)) 
    M20 = 1.0*I_2 + c_2*m_2*(c_2 + l_0*cos(q_1 + q_2) + l_1*cos(q_2)) 
    M21 = 1.0*I_2 + c_2*m_2*(c_2 + l_1*cos(q_2)) 
    M22 = 1.0*I_2 + c_2**2*m_2 

    C00 = -2.0*c_1*l_0*m_1*u_0*u_1*sin(q_1) - 1.0*c_1*l_0*m_1*u_1**2*sin(q_1) - 2.0*c_2*l_0*m_2*u_0*u_1*sin(q_1 + q_2) - 2.0*c_2*l_0*m_2*u_0*u_2*sin(q_1 + q_2) - 1.0*c_2*l_0*m_2*u_1**2*sin(q_1 + q_2) - 2.0*c_2*l_0*m_2*u_1*u_2*sin(q_1 + q_2) - 1.0*c_2*l_0*m_2*u_2**2*sin(q_1 + q_2) - 2.0*c_2*l_1*m_2*u_0*u_2*sin(q_2) - 2.0*c_2*l_1*m_2*u_1*u_2*sin(q_2) - 1.0*c_2*l_1*m_2*u_2**2*sin(q_2) - 2.0*l_0*l_1*m_2*u_0*u_1*sin(q_1) - 1.0*l_0*l_1*m_2*u_1**2*sin(q_1) 
    C10 = 1.0*c_1*l_0*m_1*u_0**2*sin(q_1) + 1.0*c_2*l_0*m_2*u_0**2*sin(q_1 + q_2) - 2.0*c_2*l_1*m_2*u_0*u_2*sin(q_2) - 2.0*c_2*l_1*m_2*u_1*u_2*sin(q_2) - 1.0*c_2*l_1*m_2*u_2**2*sin(q_2) + 1.0*l_0*l_1*m_2*u_0**2*sin(q_1) 
    C20 = c_2*m_2*(l_0*u_0**2*sin(q_1 + q_2) + l_1*u_0**2*sin(q_2) + 2*l_1*u_0*u_1*sin(q_2) + l_1*u_1**2*sin(q_2)) 

    G00 = g*(c_0*m_0*sin(q_0) + m_1*(c_1*sin(q_0 + q_1) + l_0*sin(q_0)) + m_2*(c_2*sin(q_0 + q_1 + q_2) + l_0*sin(q_0) + l_1*sin(q_0 + q_1))) 
    G10 = g*(c_1*m_1*sin(q_0 + q_1) + m_2*(c_2*sin(q_0 + q_1 + q_2) + l_1*sin(q_0 + q_1))) 
    G20 = c_2*g*m_2*sin(q_0 + q_1 + q_2)

    M[0][0] = M00
    M[0][1] = M01
    M[0][2] = M02
    M[1][0] = M10
    M[1][1] = M11
    M[1][2] = M12
    M[2][0] = M20
    M[2][1] = M21
    M[2][2] = M22
    
    C[0][0] = C00
    C[1][0] = C10
    C[2][0] = C20

    G[0][0] = G00
    G[1][0] = G10
    G[2][0] = G20

    return M, C, G
