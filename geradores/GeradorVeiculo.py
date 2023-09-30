import random
from Veiculo import Veiculo

class GeradorVeiculo:

    # Esse método tem complexidade O(1), pois o número de operações realizadas não depende do tamanho dos dados de entrada.
    def gerar_veiculos(agenteTransito, randomico):
        num_faixas = len(agenteTransito.get_faixas())
        total_veiculos_faixas = 100
        if(randomico):
        # (a) gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N objetos monitorados.
        # Nesse exemplo, os veículos são criados e adicionados nas faixas escolhidas randomicamente, para representar a dinâmica do trânsito.
        # (b) os dados gerados devem conter, obrigatoriamente, um coluna de identificação tanto para cada pessoa/objeto quanto para as leituras realizadas
            for id in range(total_veiculos_faixas):
                placa = f"ABC-{random.randint(1000, 9999)}"
                tipo = random.choice(["Carro", "Moto", "Caminhão"])
                veiculo = Veiculo(placa, tipo, id + 1)
                faixa_numero = random.randint(1, num_faixas)
                agenteTransito.monitorar_veiculo(veiculo, faixa_numero, True)
            return agenteTransito
        else:
        # (a) gerar automaticamente (randomicamente) os dados dos sensores para qualquer quantidade N objetos monitorados.
        # Nesse exemplo, os veículos são criados randomicamente e inseridos nas faixas uma a uma;
            for id in range(total_veiculos_faixas):
                placa = f"ABC-{random.randint(1000, 9999)}"
                tipo = random.choice(["Carro", "Moto", "Caminhão"])
                veiculo = Veiculo(placa, tipo, id)
                faixa_numero = id%10 + 1
                agenteTransito.monitorar_veiculo(veiculo, faixa_numero)
            return agenteTransito
            
    # (d.4) deve ser adicionada, a critério do desenvolvedor, uma funcionalidade extra, relativa ao mini-mundo escolhido, cuja
    # complexidade seja ou O(N^3) ou O(2^N) ou O(N!).
    # Esse método tem complexidade O(2^N) que é grandeza exponencial.
    # Ao receber o agenteTransito e o índice da faixa (f) que está sendo monitorada,
    # o código então passa a adicionar ou remmover de forma exponencial o número de veículos naquela faixa.
    # Isso indica que o tempo do vermelho vai ser reduzido ou acrescentado de forma exponencial também.

    def gerar_veiculos_exponencial(agenteTransito, i, f):
        for x in range(2 ** i):
            placa = f"ABC-{i}"
            tipo = "Carro"
            add = bool(random.randint(0,1))
            # add = True
            veiculo = Veiculo(placa, tipo, x)
            agenteTransito.monitorar_veiculo(veiculo, f+1, add)
        return agenteTransito
        