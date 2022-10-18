import numpy as np
import math

def deformacao(num, h, lam_ori_rad, Qg_inv, esf):

    def_lamina = np.zeros(num)
    def_lamina = def_lamina.ravel().tolist()

    def_principal = np.zeros(num)
    def_principal = def_principal.ravel().tolist()

    #-----------------------Deformação Global------------------------
    dk_global = np.dot(Qg_inv, esf.T)
    #Deformações
    def_global = np.array([[dk_global[0]], [dk_global[1]], [dk_global[2]]])
    def_global = np.reshape(def_global, (3,1))
    #Curvatura
    k_global = np.array([[dk_global[3]], [dk_global[4]], [dk_global[5]]])
    k_global = np.reshape(k_global, (3,1))

    #--------------------Deformação da Lamina---------------------   
    for lamina in range(num):
        def_lamina[lamina] = def_global + h[lamina]*k_global   

    #---------------------------Matriz R----------------------------
    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 2]])
    R_inv = np.linalg.inv(R)

    for lamina in range(num):
        m = math.cos(lam_ori_rad[lamina])
        n = math.sin(lam_ori_rad[lamina])
        T = np.array([[m**2, n**2, 2*m*n], [n**2, m**2, -2*m*n], [-m*n, m*n, (m**2 - n**2)]])
        def_principal[lamina] = np.linalg.multi_dot([R, T, R_inv, def_lamina[lamina]])

    return(def_global, k_global, def_lamina, def_principal)