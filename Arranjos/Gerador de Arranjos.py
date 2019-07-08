# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
#import matplotlib.pyplot as plt

bateria = 0.5
radio = 142.0
ch = 0
ch_count = 0
num_nodes = 250

qtd_cenarios = 33

# Variáveis usadas para plotar o gráfico dos nós
#X = list()
#Y = list()

for k in range(qtd_cenarios):
    with open('nodes' + str(k+1) + '.txt', 'w') as file:
        for i in range(1, num_nodes+1):
            x = round(np.random.uniform(0, 100), 2)
            y = round(np.random.uniform(0, 100), 2)
            #X.append(x)
            #Y.append(y)
            if (i != num_nodes):
                file.write("1`({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})++\n".format(i, bateria, x, y, radio, ch, ch_count, [], [], 0, 0, 0, [], 1, 0))
            else:
                file.write("1`({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})\n".format(i, bateria, x, y, radio, ch, ch_count, [], [], 0, 0, 0, [], 1, 0))


# =============================================================================
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.plot(X, Y, 'o')
# plt.show()
# =============================================================================

# Colocar valores genéricos para número de nós e tamanho da área
