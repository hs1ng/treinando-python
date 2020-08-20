"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento
em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
"""

duracaoSegundos = int(input("Qual o tempo de duração em segundos do evento? "))
duracaoEmHora = duracaoSegundos / 3600
duracaoEmMinutos = duracaoSegundos / 3600 * 60
duracaoEmSegundos = duracaoSegundos % 60

print(int(duracaoEmHora), ":", int(duracaoEmMinutos), ":", duracaoEmSegundos)

