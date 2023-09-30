import random
import time

from AgenteTransitoAutomatico import AgenteTransitoAutomatico
from Veiculo import Veiculo
from geradores.GeradorVeiculo import GeradorVeiculo


import matplotlib.pyplot as plt

from Plotar import Plotar

    # (c) um método main, principal, a partir do qual todas as funcionalidades possam ser executadas/testadas
def main():

    # 1. Devem ser simulados os monitoramentos de 10 pessoas/equipamentos. Exemplo: 10 pacientes ou 10 catracas;
    # Objetos monitorados = Faixas de trânsito
    num_faixas = 10

    agenteTransito = AgenteTransitoAutomatico(num_faixas)

    # Escolher a forma de inserção dos veículos nas faixas:
    randomico = True

    agenteTransito = GeradorVeiculo.gerar_veiculos(agenteTransito, randomico)

    # (d.1) imprimir a lista das pessoas ou dos objetos sendo monitorados
    # Imprimir estado inicial do semáforo
    # Nessa situação, os veículos foram alocados mas os semáforos recém iniciados estão com com o tempo pré definido.
    agenteTransito.imprimir_faixas()


    # (d.2) imprimir a lista das leituras por cada pessoa ou objeto monitorado
    # Imprimir a lista de veículos por cada faixa monitorado  
    # ATENÇÃO: deve ficar claro quais leituras pertencem a cada um;
    agenteTransito.imprimir_veiculos()

    # Ajustar o tempo de sinal vermelho
    agenteTransito.ajustar_tempo_vermelho()

    # Imprimir estado após o ajuste
    agenteTransito.imprimir_estado()

    # (d.3) ordenação crescente dos dados considerando os valores lidos dos sensores para cada coisa monitorada
    #Aqui acontece a ordenação das faixas, considerando da maior quantidade de veículos para a menor.
    agenteTransito.ordenar_faixas() 

    # Imprimindo novamente as faixas:
    agenteTransito.imprimir_faixas()

    # Passa os dados para a clase Plocar criar os graficos de visualização das alterações das faixas.
    plotador = Plotar()

   
    for f in range(len(agenteTransito.get_faixas())):
        # Arrray do tempo de vermelho da faixa
        tempos_vermelho = []
        # range_grafico = 10
        range_grafico = 10
        for i in range(range_grafico):
            agenteTransito = GeradorVeiculo.gerar_veiculos_exponencial(agenteTransito, i, f)
            agenteTransito.ajustar_tempo_vermelho()
            tempo_vermelho = agenteTransito.faixas[f].get_tempo_vermelho()
            tempos_vermelho.append(tempo_vermelho)

        # Legenda do gráfico
        titulo = f'Tempo de Sinal Vermelho vs. Número de Veículos Faixa: {f + 1}'
        label_x = 'Número de Veículos (2^N)'
        label_y = 'Tempo de Sinal Vermelho (segundos)'
        plotador.plotar_grafico(range_grafico, tempos_vermelho, titulo, label_x, label_y, f)
        print(f"Tempos de Sinal Vermelho faixa {f + 1}:", tempos_vermelho)
    plotador.show_plotagem()

        
# Chamadada do metodo
if __name__ == "__main__":
    main()



