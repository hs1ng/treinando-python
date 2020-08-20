thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])


#ADICIONA COMO ULTIMO ELEMENTO DA LISTA
thislist.append(12)
print("append = ", thislist)

#INSERE NA POSIÇÃO 3 A STRING ALGUMA COISA
thislist.insert(2, "algumacoisa")
print("insert = ", thislist)


#REMOVE PELO NOME
thislist.remove("algumacoisa")
print("remove = ", thislist)

#REMOVE PELO INDICE
thislist.pop(2)
print("pop =", thislist)

#thislist.clear()

#COPIA DA LISTA 1
mylist = thislist.copy()
print("copy = ", mylist)

#COPIA DA LISTA 2
mylist2 = list(thislist)
print(mylist2)

#OUTRO METODO PARA ADICIONAR DUAS LISTAS É ADICIONAR TODOS OS ELEMENTOS DE UMA EM OUTRA

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

#E TAMBÉM HÁ O EXTENDS

list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]

list3.extend(list4)

print("EXTENDS = ", list1)

#FAZER OUTRA LISTA UTILIZANDO O LIST

thislist = list(("apple", "banana", "maçã"))
print(thislist)
