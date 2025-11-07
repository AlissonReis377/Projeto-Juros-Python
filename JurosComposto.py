#Projeto de juros composto

import math #biblioteca reservada para funções de matematica
# #from math import pow -> importa somente a função pow da biblioteca math
import sys #biblioteca para manipulação do sistema operacional

def composto(capital, juros, tempo):
    return capital*pow((1+juros),tempo)

def simples(capital, juros, tempo):
    return capital*juros*tempo

##pegando informações sobre o investimento
capital = float(input('Qual capital de investimento?'))
juros = float(input('Qual o juros anual em porcentagem (%) ?'))
tempo = int(input('Quantos meses será o investimento?'))

##decisão se é composto ou simples
resposta = input('Deseja calcular juros composto ou simples? [C/S] ').upper()

##ajustando os valores para o calculo
juros = juros/100 #estamos dividindo por 100 para passar a porcentagem para decimal por exemplo: 3% = 3/100
tempo = tempo/12 #tempo tem que ir em ano para a equação


if resposta == 'C':
    valor_final_composto = composto(capital, juros, tempo)

    print(f'O montante final composto será de: R${valor_final_composto:.02f} ')
    print(f'O Juros do rendimento foram de: R${valor_final_composto - capital:.02f} ')

if resposta == 'S':
    valor_final_simples = simples(capital,juros,tempo)
    print(f'O montante final simples será de: R${(valor_final_simples + capital):.02f} ')
else:
    print('Opção inválida! Execute o programa novamente e escolha C ou S.')

print('Obrigado por usar nosso sistema! :D')
input('pressione ENTER para sair...')
sys.exit()
