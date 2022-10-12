import numpy as np
from regmist_input import regmist_input
from matriz import matriz
'''
OBJETIVO: Plotar a superfície de falha pelos 3 critérios e mostrar o ponto de cada lâmina. Printar se cada lâmina falhou ou não e o tipo da falha.
    -> Entrada pelas propriedades diretas ou regra das misturas;
    
CONSIDERAÇÕES:
    -> Todas as lâminas do mesmo material e mesma espessura;
'''
#----------------INÍCIO DOS INPUTS----------------
# Opções de entrada: 0-> Propriedades do material; 1->Regra das Misturas
ent_opt = 0

if ent_opt == 0:
    E1 = 77000 # MPa
    E2 = 75000 # MPa
    v12 = 0.06 
    G12 = 6500 # MPa
    props = np.array([E1, E2, v12, G12])
elif ent_opt == 1:
    Ef = 1
    Em = 1
    Vf = 0.5
    props = regmist_input(Ef, Em, Vf)
else:
    print('Opção Inválida de entrada')

Nx = 1000 # N/mm
Ny = 200 # N/mm
Nz = 0 # N/mm
Mx = 0 # N/mm
My = 0 # N/mm
Mz = 0 # N/mm
pos_lam = [0, 90, 90, 0, 45, 45]
h = 3 # mm (espessura de cada lâmina)
#----------------------FIM DOS INPUTS-----------------------
F = [Nx, Ny, Nz, Mx, My, Mz]
n_lam = np.size(pos_lam) # número de camadas
h_lam = np.zeros(n_lam+1)
E1 = props[0]
E2 = props[1]
v12 = props[2]
G12 = props[3]

if n_lam % 2 == 0: # se o numero de lâminas for PAR entra aqui
    for i in range(0 ,n_lam+1, 1):
        h_lam.itemset((i), -((n_lam/2)-i)*h)

else: # se o numero de lâminas for IMPAR entra aqui
    for i in range(0,n_lam+1, 1):
        h_lam.itemset((i), -((n_lam/2)-i)*h ) 

ABBD_inv, jureg = matriz(E1, E2, G12, v12, pos_lam, h_lam, n_lam)

print('ABBD invertida:\n', ABBD_inv)
for fiona in range(0,n_lam,1):
    print('Matriz de rigidez local da lâmina %.0f: \n' %(fiona), jureg[fiona])
