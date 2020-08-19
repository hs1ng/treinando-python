nomeDoVendedor = input("Qual o nome do vendedor? ")
salarioDoVendedor = float(input("Qual o salário do vendedor? "))
montanteTotalVendas = float(input("Qual o montante total de vendas em reais efetuado"))
comissaoVendedor = montanteTotalVendas * 0.15
totalAReceber = salarioDoVendedor + comissaoVendedor

print("O funcionário ", nomeDoVendedor, " irá receber o salário de %.2f " % totalAReceber )
