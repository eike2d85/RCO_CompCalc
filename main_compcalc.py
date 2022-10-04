import numpy as np
from regmist_input import regmist_input
'''
OBJETIVO: Plotar a superfície de falha pelos 3 critérios e mostrar o ponto de cada lâmina. Printar se cada lâmina falhou ou não e o tipo da falha.
    -> Entrada pelas propriedades diretas ou regra das misturas;
    
CONSIDERAÇÕES:
    -> Todas as lâminas do mesmo material e mesma espessura;
'''
#----------------DADOS DE ENTRADA----------------
# Opções de entrada: 0-> Propriedades do material; 1->Regra das Misturas
ent_opt = 0

if ent_opt == 0:
    E1 = 40000 # MPa
    E2 = 3000 # MPa
    v12 = 1
    G12 = 10000 # MPa
    inputs = np.array([E1, E2, v12, G12])
elif ent_opt == 1:
    Ef = 1
    Em = 1
    Vf = 0.5
    inputs = regmist_input(Ef, Em, Vf)
else:
    print('Opção Inválida de entrada')

Nx = 1000 # N/mm
Ny = 200 # N/mm
F = [Nx, Ny]
pos_lam = [0, 90, 90, 0, 45, 45]
n_lam = np.size(pos_lam) # número de camadas
h = 3 # mm (espessura de cada lâmina)

if n_lam % 2 == 0: # se o numero de lâminas for PAR entra aqui
    h_lam = np.zeros(n_lam+1)
    for i in range(0 ,n_lam+1, 1):
        h_lam.itemset((i), -((n_lam/2)-i)*h)

else: # se o numero de lâminas for IMPAR entra aqui
    h_lam = np.zeros(n_lam+1)
    for i in range(0,n_lam+1, 1):
        h_lam.itemset((i), -((n_lam/2)-i)*h ) 

print(h_lam)