import numpy as np
from regmist_input import regmist_input
'''
OBJETIVO: Plotar a superfície de falha pelos 3 critérios e mostrar o ponto de cada lâmina. Printar se cada lâmina falhou ou não e o tipo da falha.
    -> Entrada pelas propriedades diretas ou regra das misturas;
    
CONSIDERAÇÕES:
    -> Todas as lâminas do mesmo material;
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

