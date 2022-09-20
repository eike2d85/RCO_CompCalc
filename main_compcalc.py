import numpy as np
from regmist_input import regmist_input

#---------------DADOS DE ENTRADA---------------
# Opções de entrada: 0-> Propriedades do material; 1->Regra das Misturas
ent_opt = 0

if ent_opt == 0:
    E1 = 1
    E2 = 1
    v12 = 1
    G12 = 1
    inputs = np.array([E1, E2, v12, G12])
elif ent_opt == 1:
    Ef = 1
    Em = 1
    Vf = 0.5
    inputs = regmist_input(Ef, Em, Vf)
else:
    print('Opção Inválida de entrada')

