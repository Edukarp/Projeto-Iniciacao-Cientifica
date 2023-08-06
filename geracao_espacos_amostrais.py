import random
class geracao_espacos_amostrais:

    def __init__(self):
        pass

    # Gerando espaço amostral de bits de tamanho 15
    def generate_hamming_codes_15_bits(self):
        hamming_codes = []

        for i in range(2 ** 11):  # 2^11 possíveis sequências de 11 bits de informação
            binary_pattern = format(i, '0' + str(11) + 'b')  # converte para representação binária de 11 bits

            # Calcula os bits de paridade
            parity_bits = ''
            parity_bits += str((int(binary_pattern[0]) + int(binary_pattern[1]) + int(binary_pattern[3])) % 2)
            parity_bits += str((int(binary_pattern[0]) + int(binary_pattern[2]) + int(binary_pattern[3])) % 2)
            parity_bits += str((int(binary_pattern[1]) + int(binary_pattern[2]) + int(binary_pattern[3])) % 2)
            parity_bits += str((int(binary_pattern[4]) + int(binary_pattern[5]) + int(binary_pattern[6]) + int(
                binary_pattern[7]) + int(binary_pattern[8]) + int(binary_pattern[9]) + int(binary_pattern[10])) % 2)

            hamming_code = binary_pattern + parity_bits
            hamming_codes.append(hamming_code)

        return hamming_codes

    # Gerando espaço amostral de bits de tamanho 31
    def generate_hamming_codes_31_bits(self):
        binary_pattern = format(random.randint(0, 2 ** 26 - 1), '0' + str(26) + 'b')

        # Cálculo dos bits de paridade
        parity_bits = ''
        parity_bits += str((int(binary_pattern[0]) + int(binary_pattern[1]) + int(binary_pattern[3])) % 2)
        parity_bits += str((int(binary_pattern[0]) + int(binary_pattern[2]) + int(binary_pattern[3])) % 2)
        parity_bits += str((int(binary_pattern[1]) + int(binary_pattern[2]) + int(binary_pattern[3])) % 2)
        parity_bits += str((int(binary_pattern[4]) + int(binary_pattern[5]) + int(binary_pattern[6]) + int(
            binary_pattern[7]) + int(binary_pattern[8]) + int(binary_pattern[9]) + int(binary_pattern[10])) % 2)

        hamming_code = binary_pattern + parity_bits
        return hamming_code + '0'  # Adiciona um bit zero no final para totalizar 31 bits

    # Limitando o Espaco amostral para o tamanho 'size'
    def generate_space_amostral_sample_31_bits(self, size):
        space_amostral = []

        for _ in range(size):
            hamming_code = self.generate_hamming_codes_31_bits()
            space_amostral.append(hamming_code)

        return space_amostral

    # Gerando espaço amostral de bits de tamanho 63
    def generate_hamming_code_63_bits(self):
        binary_pattern = format(random.randint(0, 2 ** 57 - 1), '0' + str(57) + 'b')

        # Cálculo dos bits de paridade
        parity_bits = ''
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:8:2]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:8:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[1:8:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:16:8]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:32:16]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:64:32]) % 2))

        hamming_code = binary_pattern + parity_bits
        return hamming_code

    # Limitando o Espaco amostral para o tamanho 'size'
    def generate_space_amostral_sample_63_bits(self, size):
        space_amostral = []

        for _ in range(size):
            hamming_code = self.generate_hamming_code_63_bits()
            space_amostral.append(hamming_code)

        return space_amostral

    # Gerando espaço amostral de bits de tamanho 127
    def generate_hamming_code_127_bits(self):
        binary_pattern = format(random.randint(0, 2 ** 120 - 1), '0' + str(120) + 'b')

        # Cálculo dos bits de paridade
        parity_bits = ''
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:16:2]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:16:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:32:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:32:8]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:64:8]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:64:16]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:128:16]) % 2))

        hamming_code = binary_pattern + parity_bits
        return hamming_code

    # Limitando o Espaco amostral para o tamanho 'size'
    def generate_space_amostral_sample_127_bits(self, size):
        space_amostral = []

        for _ in range(size):
            hamming_code = self.generate_hamming_code_127_bits()
            space_amostral.append(hamming_code)

        return space_amostral

    # Gerando espaço amostral de bits de tamanho 255
    def generate_hamming_code_255_bits(self):
        binary_pattern = format(random.randint(0, 2 ** 247 - 1), '0' + str(247) + 'b')

        # Cálculo dos bits de paridade
        parity_bits = ''
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:32:2]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:32:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:64:4]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:64:8]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:128:8]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:128:16]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:256:16]) % 2))
        parity_bits += str((sum(int(bit) for bit in binary_pattern[0:256:32]) % 2))

        hamming_code = binary_pattern + parity_bits
        return hamming_code

    # Limitando o Espaco amostral para o tamanho 'size'
    def generate_space_amostral_sample_255_bits(self, size):
        space_amostral = []

        for _ in range(size):
            hamming_code = self.generate_hamming_code_255_bits()
            space_amostral.append(hamming_code)

        return space_amostral