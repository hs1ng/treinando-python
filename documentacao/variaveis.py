"""Criação de variáveis
Variáveis ​​são contêineres para armazenar valores de dados.

Ao contrário de outras linguagens de programação, Python não tem comando para declarar uma variável.

Uma variável é criada no momento em que você atribui um valor a ela.

x = 5
y = "John"
print(x)
print(y)

---------------------------------------------------------------------------------

As variáveis ​​não precisam ser declaradas com nenhum tipo específico e podem até mesmo mudar de tipo após terem sido definidas.
x = 4  -> x é do tipo inteiro
x = "Sally" # x agora é do tipo String
print(x)

---------------------------------------------------------------------------------

Variáveis ​​de string podem ser declaradas usando aspas simples ou duplas:

x = "John"
# é o mesmo que
x = 'John'

---------------------------------------------------------------------------------

----Nomes de Variáveis
----Uma variável pode ter um nome curto (como xey) ou um nome mais descritivo 
----(idade, carname, total_volume). Regras para variáveis ​​Python:
----Um nome de variável deve começar com uma letra ou o caractere de sublinhado
----Um nome de variável não pode começar com um número
----Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _)
----Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas 
----(idade, idade e IDADE são três variáveis ​​diferentes)

Exemplo
#Legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Ilegal
2myvar = "John"
my-var = "John"
my var = "John"

---------------------------------------------------------------------------------

----Atribuir valor a várias variáveis
----Python permite que você atribua valores a várias variáveis ​​em uma linha:

Exemplo
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

---------------------------------------------------------------------------------
E você pode atribuir o mesmo valor a várias variáveis ​​em uma linha:
x = y = z = "Orange"
print(x)
print(y)
print(z)

---------------------------------------------------------------------------------

Variáveis ​​de saída
A instrução print Python costuma ser usada para gerar variáveis.

----Para combinar texto e variável, Python usa o + :
Exemplo
x = "awesome"
print("Python is " + x)


----Você também pode usar o + para adicionar uma variável a outra variável:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

----Para números, o +  funciona como um operador matemático

x = 5
y = 10
print(x + y)

----Se você tentar combinar uma string e um número, o Python apresentará um erro:

x = 5
y = "John"
print(x + y)

---------------------------------------------------------------------------------

Variáveis ​​que são criadas fora de uma função (como em todos os exemplos acima) são conhecidas como variáveis ​​globais.

Variáveis ​​globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.

----Exemplo
----Crie uma variável fora de uma função e use-a dentro da função

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

----Se você criar uma variável com o mesmo nome dentro de uma função, 
----essa variável será local e só pode ser usada dentro da função. 
----A variável global com o mesmo nome permanecerá como era, global e com o valor original.

Exemplo
Crie uma variável dentro de uma função, com o mesmo nome da variável global

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""