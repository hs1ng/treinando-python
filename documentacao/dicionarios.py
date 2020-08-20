"""Um dicionário é uma coleção
 não ordenada, alteravel e indexada. No Python, os dicionários são escritos com chaves e têm chaves e valores.
 
Exemplo
Crie e imprima um dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

Você pode acessar os itens de um dicionário referindo-se ao nome da chave, entre colchetes:

Exemplo
Obtenha o valor da chave "model":

x = thisdict["model"]

Também existe um método chamado get() que fornecerá o mesmo resultado:

Exemplo
Obtenha o valor da chave "model":

x = thisdict.get("model")


Mudar valores
Você pode alterar o valor de um item específico, referindo-se ao seu nome de chave:

Exemplo
Altere o "ano" para 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


Percorrer um dicionário
Você pode percorrer um dicionário usando um for.

Ao percorrer um dicionário, os valores de retorno são as chaves do dicionário, 
mas também existem métodos para retornar os valores .

Exemplo
Imprima todos os nomes de chave no dicionário, um por um:

for x in thisdict:
  print(x)
 

Exemplo
Imprima todos os valores do dicionário, um por um:

for x in thisdict:
  print(thisdict[x]) 


Exemplo
Você também pode usar o values()método para retornar valores de um dicionário:

for x in thisdict.values():
  print(x)

Exemplo
Loop através de chaves e valores , usando o items()método:

for x, y in thisdict.items():
  print(x, y)
  

Verifique se a chave existe
Para determinar se uma chave especificada está presente em um dicionário, use a in:

Exemplo
Verifique se "modelo" está presente no dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

Comprimento do Dicionário
Para determinar quantos itens (pares de valores-chave) um dicionário possui, use a len() função.

Exemplo
Imprima o número de itens no dicionário:

print(len(thisdict))


Adicionando Itens
Adicionar um item ao dicionário é feito usando uma nova chave de índice e atribuindo um valor a ela:

Exemplo
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"] = "red"
print(thisdict)


Removendo itens
Existem vários métodos para remover itens de um dicionário:

Exemplo
O pop()método remove o item com o nome de chave especificado:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


Exemplo
O popitem() remove o último item inserido (nas versões anteriores à 3.7, um item aleatório é removido):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


Exemplo
A del remove o item com o nome de chave especificado:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) -> isso causará um erro por thisdict não existe mais.


Exemplo
O clear() esvazia o dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



Copiar um Dicionário
Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2
será apenas uma referência a dict1 e as alterações feitas em dict1 também serão feitas automaticamente em dict2.

Existem maneiras de fazer uma cópia, uma delas é usar o método interno do Dicionário copy().

Exemplo
Faça uma cópia de um dicionário com o copy()método:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


Outra maneira de fazer uma cópia é usar a função interna dict().

Exemplo
Faça uma cópia de um dicionário com a dict() função:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


Dicionários aninhados
Um dicionário também pode conter muitos dicionários, isso é chamado de dicionários aninhados.

Exemplo
Crie um dicionário que contenha três dicionários:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


Ou, se você deseja aninhar três dicionários que já existem como dicionários:

Exemplo
Crie três dicionários e, em seguida, crie um dicionário que conterá os outros três dicionários:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

-Dicionario que contém os outros 3 dicionários-
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


O construtor dict ()
Também é possível usar o construtor dict () para fazer um novo dicionário:

Exemplo
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# observe que palavras-chave não são literais de string
# observe o uso de igual em vez de dois pontos para a atribuição
print(thisdict)


Métodos de Dicionário
Python tem um conjunto de métodos embutidos que você pode usar em dicionários.

Descrição dos métodos {
clear()	Remove todos os elementos do dicionário
copy()	Retorna uma cópia do dicionário
fromkeys() Retorna um dicionário com as chaves e valores especificados
get() Retorna o valor da chave especificada
items()	Retorna uma lista contendo uma tupla para cada par de valores-chave
keys() Retorna uma lista contendo as chaves do dicionário
pop() Remove o elemento com a chave especificada
popitem() Remove o último par de valores-chave inserido
setdefault() Retorna o valor da chave especificada. Se a chave não existe: insira a chave, com o valor especificado
update() Atualiza o dicionário com os pares de valores-chave especificados
values() Retorna uma lista de todos os valores do dicionário
}
"""
 
 