#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida
#(em Km) e o total de combustível gasto (em litros)

#Entrada

distanciaTotal = int(input("Qual a distância percorrida em KM? "))
totalCombustivelGasto = float(input("Qual o total de combustível gasto em litros? "))

consumoMedio = distanciaTotal / totalCombustivelGasto

print("O consumo médio para a distancia de", distanciaTotal, "e para o gasto de combustível de", totalCombustivelGasto, "será de %.3f km/1" % consumoMedio)