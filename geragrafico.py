from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt
 
def main():
    leitor = LeitorArquivo('data.text')
    valores = leitor.getValores()
    plt.title('Gráfico de linhas')
    print(valores)
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    for serie in valores:
       plt.plot(serie)
    plt.show()
 
main()
