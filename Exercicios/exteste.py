import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.log(x + 1)

# Criando uma figura e um conjunto de subplots
fig, ax1 = plt.subplots()

# Gráfico de linha para y1
ax1.plot(x, y1, 'g-')
ax1.set_xlabel('Eixo X (x)')
ax1.set_ylabel('Sen(x)', color='g')

# Criando um segundo eixo Y que compartilha o mesmo eixo X
ax2 = ax1.twinx()
ax2.plot(x, y2, 'b-')
ax2.set_ylabel('log(x+1)', color='b')

plt.title('Gráfico de Linhas com Múltiplos Eixos')
plt.show()

