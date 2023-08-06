import random
import numpy as np

from geracao_espacos_amostrais import Geracao_espacos_amostrais
from funcoes_corretoras import Funcoes_corretoras
from funcoes_geradoras import Funcoes_geradoras
from plotagem import Plotagem

# Variaveis definidas

#Definindo constantes de Canal e Ruido
media = 0.5
variancia = 1.5

#Definindo tipos para a cadeia de bits inicial X
x = []
auxX = []

#Definindo tipos para o ganho do canal dos receptores 1, 2 e 3
h = [] #ganho do canal dos receptores 1 e 2 (proximos)
h3 = [] #ganho do canal do receptor 3 (mais distante)

#Criando arrays de erros para calcular a media
arrayErrorsy1 = []
arrayErrorsy2 = []
arrayErrorsy3 = []
contagemDeAcertos = 0 #Conta quantas vezes os bits foram iguais ao final do processo

#Objetos para utilização das funcoes
espaçosAmostrais = Geracao_espacos_amostrais()
funcoesGeradoras = Funcoes_geradoras()
funcoesCorretoras = Funcoes_corretoras()
funcoesPlotagem = Plotagem()

# Definindo o numero de Bits e o espaco amostral
print("Entre com um dos valores possiveis para o tamanho da cadeia de Bits")
comando = int(input("Digite: '1' para 7 Bits, '2' para 15 Bits, '3' para 31 Bits, '4' para 63 Bits "
      ", '5' para 127 Bits ou '6' para 255 Bits "))
if comando == 1:
    nBits = 7
    #Espaco amostral de 7 Bits ja definido
    tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                        '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
elif comando == 2:
    nBits = 15
    tabela = espaçosAmostrais.generate_hamming_codes_15_bits()
    print(tabela)

elif comando == 3:
    nBits = 31
    tabela = espaçosAmostrais.generate_space_amostral_sample_31_bits(int(input("Digite o tamanho da amostra: ")))

elif comando ==  4:
    nBits = 61
    tabela = espaçosAmostrais.generate_space_amostral_sample_63_bits(int(input("Digite o tamanho da amostra: ")))

elif comando == 5:
    nBits = 127
    tabela = espaçosAmostrais.generate_space_amostral_sample_127_bits(int(input("Digite o tamanho da amostra: ")))

elif comando == 6:
    nBits = 255
    tabela = espaçosAmostrais.generate_space_amostral_sample_255_bits(int(input("Digite o tamanho da amostra: ")))
else:
    print("Tamanho Invalido, processo encerrado.")
    exit()

# Definindo o numero de testes
nTestes = int(input("Entre com o numero de testes: "))
#Crinado arrayTestes e preenchendo para a plotagem
arrayTestes = []
for i in range(nTestes):
    arrayTestes.append(i)

# Gerando a cadeia de bits aleatorios inicial X
for i in range(nBits):
    x.append(random.randint(0, 1))
auxX = x.copy()

# Gerando o ganho de canal de maneira Rayleigh
size = nBits # tamanho da amostra
scale = 1.0 #escala da distribuição (parâmetro sigma)
h = np.random.rayleigh(scale, size)  #ganho do canal dos receptores 1 e 2
scale3 = 0.5 #escala da distribuição menor para o mais distante (menor ganho do canal)
h3 = np.random.rayleigh(scale3, size)  #ganho do canal do receptor 3 (distante)

# Opcao de Plotagem
comando = input("Deseja realizar a Plotagem dos sinais? 'y' para sim, 'n' para nao ")
if comando == 'y':
    plot = 1
else:
    plot = 0

# Iniciando o Procsso
for j in range(nTestes):

    #Redefinindo as cadeias a cada passagem
    y1 = [] #btis finais do receptor 1
    y2 = []  # btis finais do receptor 2
    y3 = []  # btis finais do receptor 3
    auxY = [] #Aux para ploatagem dos bits em Y
    print('x  =', x)

    #Gerando ruido Rayleigh e seus Y's para cada variancia no receptor 1 e 2 (proximos)
    y1 = funcoesGeradoras.calculaY(h, x, variancia-1.3, media, nBits) #Variancia Reduzida para diminuir ruido ao mais proximo
    print('y1 =', y1)
    y2 = funcoesGeradoras.calculaY(h, x, variancia-1.3, media, nBits)
    print('y2 =', y2)

    #Gerando ruido Rayleigh e seu Y para cada variancia no receptor 3 (distante)
    y3 = funcoesGeradoras.calculaY(h3, x, variancia+1, media, nBits) #Variancia Aumentada para acrescentar ruido ao mais distante
    print('y3 =', y3)

    #Encontrando as disparidades
    arrayErrorsy1.append(funcoesCorretoras.encontraErrors(x, y1))
    arrayErrorsy2.append(funcoesCorretoras.encontraErrors(x, y2))
    arrayErrorsy3.append(funcoesCorretoras.encontraErrors(x, y3))

    #Covertendo os arrays para String para fazer a comparacao
    toStringY1 = ''.join(map(str, y1))
    toStringY2 = ''.join(map(str, y2))
    toStringY3 = ''.join(map(str, y3))

    #Se a plotagem estiver habilitada
    if plot:
        # Ajeitando a Plotagem
        auxX = x.copy()
        x = funcoesPlotagem.fixPlot(auxX)
        auxY = y1.copy()
        y1 = funcoesPlotagem.fixPlot(auxY)
        auxY = y2.copy()
        y2 = funcoesPlotagem.fixPlot(auxY)
        auxY = y3.copy()
        y3 = funcoesPlotagem.fixPlot(auxY)

        # Definindo tamanho e plotando
        tam = list(range(0, len(x)))
        funcoesPlotagem.plota_diferencas(x, y1,y2, tam)  #plotando a comapracao de X com Y1 e Y2

    #Correcao e Mostragem dos Erros
    print('Quantidade de erros em y1: ', arrayErrorsy1[j])
    print('Porcentagem de erros em y1: ', int(arrayErrorsy1[j]/len(auxX)*100), end='%\n')
    P = funcoesCorretoras.encontraParidade(toStringY1, tabela)

    print('Quantidade de erros em y2: ', arrayErrorsy2[j])
    print('Porcentagem de erros em y2: ', int(arrayErrorsy2[j]/len(auxX)*100), end='%\n')
    Key = funcoesCorretoras.comparaSinais(toStringY2, P, tabela)

    print('Quantidade de erros em y3: ', arrayErrorsy3[j])
    print('Porcentagem de erros em y3: ', int(arrayErrorsy3[j]/len(auxX)*100), end='%\n')
    #print('Codigo Corrigido em y3: ', comparacao_mais_proxima(toStringY3))

    #Realiza a Comparacao de Y1 e Y2
    print("\n Comparcao de Y1 e Y2:")
    print("Y1 = ", toStringY1, " Y2 = ", toStringY2)
    print("Apos Passagem Y2/ChaveFinal ficou = ", Key)

    x = auxX.copy() #Aux para retornar x ao seu valor inicial

    #Verifica se ao final os bits são iguais e adiciona um valor a contagem
    if (toStringY1 == Key):
        print("Sao iguais")
        contagemDeAcertos += 1
    else:
        print("Nao sao iguais")

    print("\n--------------------------------------------------------")

# Printando Medias Finais
print(f'Media de erros do Receptor Y1: {(np.mean(arrayErrorsy1)*100)/nBits:.2f}',end='%\n')
print(f'Media de erros do Receptor Y2: {(np.mean(arrayErrorsy2)*100)/nBits:.2f}',end='%\n')
print(f'Media de erros do Receptor Y3: {(np.mean(arrayErrorsy3)*100)/nBits:.2f}',end='%\n')
print(f'Media de Bits Iguais dos Receptore Y1 e Y2: {contagemDeAcertos*100.0/nTestes:.2f}',end='%\n')

# Plota comparacao de erros finais
if plot:
    funcoesPlotagem.plota_errors(arrayTestes, arrayErrorsy1, arrayErrorsy2, arrayErrorsy3)


