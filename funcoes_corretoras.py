class funcoes_corretoras:

    def __init__(self):
        pass

    def hamming_distance(self, s1, s2):
        assert len(s1) == len(s2)
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    def subtract_binary(self, fc, y):
        assert len(fc) == len(y), "Os valores devem ter o mesmo número de dígitos binários."

        result = ""
        for i in range(len(fc)):
            if fc[i] == y[i]:
                result += "0"
            else:
                result += "1"

        return result

    def xor_binary(self, fc, P):
        assert len(fc) == len(P), "Os valores devem ter o mesmo número de dígitos binários."

        result = ""
        for i in range(len(fc)):
            if fc[i] == P[i]:
                result += "0"
            else:
                result += "1"

        return result

    # Funcao para comparacao entre Y1 e espaco amostral retornando P
    def encontraParidade(self, y, tabela):
        fc = self.comparacao_mais_proxima(y, tabela)
        P = self.subtract_binary(fc, y)
        return P

    def comparaSinais(self, y, P, tabela):
        fc = self.comparacao_mais_proxima(self.subtract_binary(y, P), tabela)
        y = self.xor_binary(P, fc)
        return y

    def comparacao_mais_proxima(self, y, tabela):
        pos = 0
        min = 99999

        for i in range(len(tabela)):
            aux = self.hamming_distance(str(y), str(tabela[i]))
            if aux < min:
                pos = i
                min = aux

        return tabela[pos]