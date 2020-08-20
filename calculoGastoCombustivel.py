"""Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma
viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o
auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o
tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h).
Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam
necessários. Mostre o valor com 3 casas decimais após o ponto.
"""

tempoGasto = int(input("Em quantas horas será completada a viagem? "))
velocidadeMedia = int(input("Qual a velocidade média por km percorrida pelo carro? "))

calculoGastoCombustivel = tempoGasto * velocidadeMedia / 12

print("A quantidade de litros necessária para a sua viagem é: %.3f" % calculoGastoCombustivel)