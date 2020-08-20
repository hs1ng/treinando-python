"""Tupla
Uma tupla é uma coleção ordenada e inalteravel . Em Python, as tuplas são escritas com colchetes.

Exemplo
Crie uma tupla:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

////////////////Acessar itens de tupla////////////////
Você pode acessar itens de tupla referindo-se ao número do índice, entre colchetes:

Exemplo
Imprima o segundo item na tupla:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

////////////////Indexação Negativa////////////////
Indexação negativa significa começar do fim, -1refere-se ao último item, -2refere-se ao penúltimo item etc.
Exemplo
Imprima o último item da tupla:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


////////////////Faixa de índices negativos////////////////
Especifique índices negativos se você deseja iniciar a pesquisa a partir do final da tupla:

Exemplo
Este exemplo retorna os itens do índice -4 (incluído) para o índice -1 (excluído)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


////////////////Alterar os valores da tupla////////////////
Depois que uma tupla é criada, você não pode alterar seus valores. As tuplas são imutáveis ou imutáveis, como também são chamadas.

Mas há uma solução alternativa. Você pode converter a tupla em uma lista, alterar a lista e converter a lista novamente em uma tupla.

////////////////Exemplo
Converta a tupla em uma lista para poder alterá-la:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

o tuple transforma a lista em tupla

print(x)

////////////////Loop através de uma tupla////////////////
Você pode percorrer os itens da tupla usando um forloop.

Exemplo
Repita os itens e imprima os valores:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


////////////////Verifique se o item existe////////////////
Para determinar se um item especificado está presente em uma tupla, use in:

Exemplo
Verifique se "apple" está presente na tupla:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  
////////////////Comprimento da Tupla////////////////
Para determinar quantos itens uma tupla tem, use o len():

Exemplo
Imprima o número de itens na tupla:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


////////////////Criar tupla com um item////////////////
Para criar uma tupla com apenas um item, você precisa adicionar uma vírgula após o item, caso contrário, o Python não a reconhecerá como uma tupla.

Exemplo
Tupla de um item, lembre-se da vírgula:

thistuple = ("apple",)
print(type(thistuple))

#Não é uma tupla
thistuple = ("apple")
print(type(thistuple))


////////////////Remover itens////////////////
Nota: Você não pode remover itens em uma tupla.

As tuplas são imutáveis , então você não pode remover itens dela, mas pode excluir a tupla completamente:

Exemplo
A delpalavra-chave pode excluir a tupla completamente:

thistuple = ("apple", "banana", "cherry")
del thistuple


////////////////Junte-se a duas tuplas////////////////
Para juntar duas ou mais tuplas, você pode usar o + operador:

Exemplo
Junte duas tuplas:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

////////////////O construtor tupla////////////////
Também é possível usar o construtor tuple() para fazer uma tupla.

Exemplo
Usando o método tuple() para fazer uma tupla:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

"""