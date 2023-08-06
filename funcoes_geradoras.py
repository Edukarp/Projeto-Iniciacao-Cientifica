import random

class Funcoes_geradoras:

    def __init__(self):
        pass

    def geraRuido(self, variancia, media, ntestes):
        n = {}  # Ruido Gaussiano
        n = list(n)
        for i in range(ntestes):
            n.append(random.gauss(media, variancia))
        return n

        return errors
    def calculaY(self, h, x, variancia, media, ntestes):
        y = {}
        y = list(y)
        n = self.geraRuido(variancia, media, ntestes)

        for i in range(ntestes):
            y.append(h[i] * x[i] + n[i])  # gerando o bit final pela operacao matematica
            if y[i] <= 0.5:
                y[i] = 0
            else:
                y[i] = 1
        return y