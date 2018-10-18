import numpy as np
import pandas as pd
import random as rd

pessoas = []
N = 100

for i in range(N):
    pessoas.append([rd.uniform(1.5, 2.1), rd.uniform(50, 100)])

pessoas = np.array(pessoas)

combinacoes = []
classe = np.array([0])

for i in range(N):
    for j in range(N):
        imc1 = pessoas[i][1] / pessoas[i][0]**2
        imc2 = pessoas[j][1] / pessoas[j][0]**2
        if imc1 > imc2:
            classe[0] = -1
        elif imc2 > imc1:
            classe[0] = 1
        else:
            classe[0] = 0
        linha = np.concatenate((pessoas[i], pessoas[j], classe))
        combinacoes.append(linha)

combinacoes = np.array(combinacoes)


base = pd.DataFrame(combinacoes, columns=['altura1', 'peso1', 'altura2', 'peso2', 'classe'])

base.to_csv('base.csv', index = False)