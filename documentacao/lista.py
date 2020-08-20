"""Coleções Python (matrizes)
Existem quatro tipos de dados de coleção na linguagem de programação Python:

////Lista é uma coleção ordenada e mutável. Permite membros duplicados.
////Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
///Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
Dicionário é uma coleção não ordenada, mutável e indexada. Nenhum membro duplicado.
Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo.
Escolher o tipo certo para um determinado conjunto de dados pode significar retenção de significado e, 
pode significar um aumento na eficiência ou segurança.
"""

"""
Lista
Uma lista é uma coleção ordenada e mutável. Em Python, as listas são escritas com colchetes.

Exemplo
Crie uma lista:

thislist = ["apple", "banana", "cherry"]
print(thislist)





//////////////////////////////////Itens de acesso/////////////////////////////
Você acessa os itens da lista referindo-se ao número do índice:

EX: Imprima o segundo item da lista:

thislist = ["apple", "banana", "cherry"]
-> print(thislist[1]) -> retorna apple





///////////////////////////////////Indexação Negativa/////////////////////////////
Indexação negativa significa começar do fim, -1 refere-se ao último item, -2 refere-se ao penúltimo item etc.

Exemplo
Imprima o último item da lista:

thislist = ["apple", "banana", "cherry"]
-> print(thislist[-1]) -> imprime cherry





////////////////////////////////////Gama de índices/////////////////////////////
Você pode especificar um intervalo de índices, especificando onde começar e onde terminar o intervalo.

Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.

Exemplo
Devolva o terceiro, quarto e quinto item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
-> print(thislist[2:5])
Nota: A pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).

Ao omitir o valor inicial, o intervalo começará no primeiro item:

Exemplo
Este exemplo retorna os itens do início para "laranja":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
-> print(thislist[:4])

----

Ao omitir o valor final, o intervalo irá para o final da lista:

Exemplo
Este exemplo retorna os itens de "cereja" e até o final:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])



/////////////////Adicionar itens/////////////////////////////
Para adicionar um item ao final da lista, use o método append () :

Exemplo
Usando o append()método para anexar um item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



////////////////Para adicionar um item no índice especificado, use o método insert () ://////////////

Exemplo
Insira um item como a segunda posição:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

///////////////////////Remover item
Existem vários métodos para remover itens de uma lista:

Exemplo
O remove() remove o item especificado:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

Exemplo
O pop() remove o índice especificado (ou o último item se o índice não for especificado):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

Exemplo
A del remove o índice especificado:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

A del também pode excluir a lista completamente:

thislist = ["apple", "banana", "cherry"]
del thislist


Exemplo
O clear() esvazia a lista:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


/////////////////////Copiar uma lista/////////////////////////////
Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2 será 
apenas uma referência a list1 e as alterações feitas em list1 também serão feitas automaticamente em list2.

Existem maneiras de fazer uma cópia, uma delas é usar o método interno List copy().

Exemplo
Faça uma cópia de uma lista com o copy():

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Outra maneira de fazer uma cópia é usar o método interno list().

Exemplo
Faça uma cópia de uma lista com o list():

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

>>>>>>>>>>>>>>>Outra maneira de juntar duas listas é anexar todos os itens da lista2 à lista1, um por um:

Exemplo
Anexe a lista2 à lista1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

Ou você pode usar o extend() método, cujo objetivo é adicionar elementos de uma lista a outra lista:
Exemplo
Use o extend() para adicionar list2 ao final de list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

>>>>>>>>>>>>>Também é possível usar o construtor list () para fazer uma nova lista.

Exemplo
Usando o list()construtor para fazer uma lista:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""