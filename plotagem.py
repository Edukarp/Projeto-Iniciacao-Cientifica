import matplotlib.pyplot as plt
class Plotagem:

    def __init__(self):
        pass

    # grafico comparando diferença de X e Y
    def plota_diferencas(self, x, y1, y2, tam):
        plt.subplot(2, 1, 1)
        plt.plot(tam, x, 'r--')
        plt.plot(tam, y1)
        plt.title('Y1')

        plt.subplot(3, 1, 3)
        plt.plot(tam, x, 'r--')
        plt.plot(tam, y2)
        plt.title('Y2')

        plt.show()

    # grafico comparando a quantidade de erros entre as variancias e os receptores
    def plota_errors(self, arraytestes, quantErrorsy1, quantErrorsy2, quantErrorsy3):
        plt.xlabel('Quantidade de Testes')
        plt.ylabel('Quantidade de Erros')
        plt.title('Quantidade de erros por Y')
        plt.plot(arraytestes, quantErrorsy1, label='Y1')
        plt.plot(arraytestes, quantErrorsy2, label='Y2')
        plt.plot(arraytestes, quantErrorsy3, label='Y3')
        plt.show()


    def fixPlot(self, aux):
        y = {}
        y = list(y)
        for i in range(len(aux)):
            for k in range(100):
                y.append(aux[i])

        return y