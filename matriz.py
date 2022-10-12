import numpy as np
import math

def matriz(E1, E2, G12, P12, lam_ori, h, num): #P12 é o poisson

    Qkg = np.zeros(num)
    Qkg = Qkg.ravel().tolist()
#---------------------------Matriz de Rigidez----------------------------
    Q11 =  E1**2/(E1-E2*P12**2)
    Q22 = E1*E2/(E1-E2*P12**2)
    Q66 = G12
    Q12 = (P12*E1*E2/(E1-E2*P12**2))
    Q = np.array([[Q11, Q12, 0], [Q12, Q22, 0], [0, 0, Q66]])

#---------------------------Matriz de Reuter----------------------------
    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 2]])
    R_inv = np.linalg.inv(R)
#---------------------Matriz de Rigidez Transformada---------------------
    lam_ori = np.array(lam_ori)
    lam_ori = (math.pi/180)*lam_ori
    for lamina in range(num):
        m = math.cos(lam_ori[lamina])
        n = math.sin(lam_ori[lamina])
        T = np.array([[m**2, n**2, 2*m*n], [n**2, m**2, -2*m*n], [-m*n, m*n, (m**2 - n**2)]])
        T_inv = np.linalg.inv(T)
        Qkg[lamina] = np.linalg.multi_dot([T_inv, Q, R, T, R_inv])
#------------------------------Matriz ABBD------------------------------
    A_h_dif = np.zeros(num)
    B_h_dif = np.zeros(num)
    D_h_dif = np.zeros(num)
    A_prod = np.zeros(num).ravel().tolist()
    B_prod = np.zeros(num).ravel().tolist()
    D_prod = np.zeros(num).ravel().tolist()

    for k in range(num):
        A_h_dif[k] = (h[k+1] - h[k])
        B_h_dif[k] = (h[k+1]**2 - h[k]**2)
        D_h_dif[k] = (h[k+1]**3 - h[k]**3)

        A_prod[k] = A_h_dif[k]*Qkg[k]
        B_prod[k] = B_h_dif[k]*Qkg[k]
        D_prod[k] = D_h_dif[k]*Qkg[k]

    A = sum(A_prod)
    B = sum(B_prod)/2
    D = sum(D_prod)/3

#---------------------------Matriz ABBD ---------------------------
    Qg_l = np.array([[A[0][0], A[0][1], A[0][2], B[0][0], B[0][1], B[0][2]], 
                    [A[1][0], A[1][1], A[1][2], B[1][0], B[1][1], B[1][2]], 
                    [A[2][0], A[2][1], A[2][2], B[2][0], B[2][1], B[2][2]],
                    [B[0][0], B[0][1], B[0][2], D[0][0], D[0][1], D[0][2]], 
                    [B[1][0], B[1][1], B[1][2], D[1][0], D[1][2], D[1][2]], 
                    [B[2][0], B[2][1], B[2][2], D[2][0], D[2][1], D[2][2]]])

    Qg_l_inv = np.linalg.inv(Qg_l)

    return(Qg_l_inv,Qkg)