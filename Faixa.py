# Os objetos monitorados serão as Faixas, que terá um número de veículos e para cada Faixa, quando o número de veículos aumentar ou diminuir, o tempo do semáforo na cor vermelha vai ser alterado, evitando engarrafamentos.
# Classe para simular o objeto monitorado, cuja complexidade, de forma geral, é O(1)

class Faixa:
    # (b) os dados gerados devem conter, obrigatoriamente, um coluna de identificação tanto para cada pessoa/objeto quanto para as leituras realizadas
    #O objeto é inciado com um número, que serve de identificador único e um tempo de vermelho, pré-determinado e 20 segundos o valor mínimo.
    def __init__(self, numero, tempo_vermelho):
        self.numero = numero
        self.tempo_vermelho = tempo_vermelho
        self.veiculos = []
    
    def get_numero(self):
        return self.numero
    
    def get_tempo_vermelho(self):
        return self.tempo_vermelho
    
    def get_veiculos(self):
        return self.veiculos

    #Adiciona um veículo na faixa:
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    # ou
    #remover um veículo na faixa:
    def remover_veiculo(self, veiculo):
        if len(self.veiculos) != 0:
            self.veiculos.pop()

    #Caso exista variação na quantidade de veículos, um novo tempo de vermelho deve ser calculado. A oscilação é atribuido para alterar o tempo de vermelho em uma proporção referente ao número de veículos da faixa.
    def calcular_tempo_vermelho(self):
        base_tempo = 30  
        oscilacao = .02
        # oscilacao = .02  
        tempo_minimo = 20

        # tempo_minimo = 20

        tempo_calculado = base_tempo - (len(self.veiculos)* oscilacao)

        # return tempo_calculado
        # Garante que o tempo de vermelho não seja menor que 20 segundos
        if tempo_calculado < tempo_minimo:
            return tempo_minimo
        else:
            return tempo_calculado

    def __str__(self):
        return f"Faixa {self.numero}: Tempo Vermelho={self.tempo_vermelho}s, Veículos={len(self.veiculos)}"