# Configuração do grafico apresentado
import matplotlib.pyplot as plt

class Plotar:

    def plotar_grafico(self, range_grafico, tempos_vermelho, titulo, label_x, label_y, f):
        plt.title(titulo)
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.figure(f + 1)
        plt.grid(True)
        plt.plot(range(range_grafico), tempos_vermelho, marker='o')

       

    def show_plotagem(self):
        plt.show()      