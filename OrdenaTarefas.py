import pandas as pd

# base contendo comparacoes entre pessoas diferentes
# compara quem tem maior imc

# -1 significa que é a pessoa A
# 0 significa que são iguais
# 1 significa que é a pessoa B

base = pd.read_csv('base.csv')

# Separar as atributos previsores da classe
classe = base.pop(base.keys()[-1])
previsores = base.values

#%% Padronizar os dados

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler_previsores = scaler.fit(previsores)
previsores2 = scaler_previsores.transform(previsores)

#%% Machine learning

from sklearn.neural_network import MLPRegressor

modelo = MLPRegressor(hidden_layer_sizes = (50, 30), learning_rate = 'adaptive', max_iter = 1000)

# Ensinando rede neural
modelo.fit(previsores2, classe)

## Predição dos rótulos das instâncias de teste
#classe_predita = modelo.predict(previsoresValidacao[test])

#%% Ordenar pessoas pelo IMC

import numpy as np

# Formato: altura, peso
pessoas = []
pessoas.append([1.6, 55])
pessoas.append([1.7, 69])
pessoas.append([1.65, 70])
pessoas.append([1.85, 100])
pessoas.append([1.9, 97])
pessoas.append([1.5, 45])

pessoas = np.array(pessoas)

# Testar comparacao entre duas pessoas
comparacao = [np.concatenate((pessoas[0], pessoas[4]))]
comparacao = scaler_previsores.transform(comparacao)
predicao = modelo.predict(comparacao)


#%% Definir callback da ordenação

#Compara duas pessoas e vê quem é tem maior IMC, sem calcular IMC
def compare(item1, item2):
    comparacao = [np.concatenate((item1, item2))]
    comparacao = scaler_previsores.transform(comparacao)
    return modelo.predict(comparacao)

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

#%% ordenar pelo IMC
# Lembrando, a rede neural não sabe calcular o IMC
# Ela só sabe comparar duas pessoas e dizer quem tem maior IMC

pessoas_ordenadas = sorted(pessoas, key=cmp_to_key(compare))
pessoas_ordenadas = np.array(pessoas_ordenadas)

# imprimir resultado

for pessoa in pessoas_ordenadas:
    imc = pessoa[1] / pessoa[0]**2
    print("Peso: %.2f Altura: %.2f IMC: %f" %(pessoa[1], pessoa[0], imc))
