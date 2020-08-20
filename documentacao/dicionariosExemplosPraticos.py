#criando dicionario

thisdict = {"nome": "hsing",
            "estudante": "sim"}
print(thisdict)


#Acessando item do dicionário
x = thisdict["nome"]

print(x)

#Acessando item através do metodo get

x = thisdict.get("nome")
print("Através do metodo get", x)

#Alterando valor de um item do dicionario

thisdict["estudante"] = "não"
print(thisdict)

#percorrendo um dicionário
#imprimindo todos os nomes de chave do dicionario, um por um

for x in thisdict:
    print("Nomes = ",x)
    
#imprimindo os valores do dicionario, um por um

for x in thisdict:
    print("Valores = ",thisdict[x])
    
#imprimindo chave e valor, através do metodo items
for x,y in thisdict.items():
    print("Utilizando o metodo items: ",x, "=",y)
    
    
#verificando se o nome-chave existe    
if "estudante" in thisdict:
    print("Sim, o nome-chave estudante existe.")
    
#imprimindo o comprimento do dicionario

print("Comprimento do dicionario:",len(thisdict))

#adicionando items

thisdict["faculdade"] = "UFF"
thisdict["estudante"] = "sim"

print(thisdict)

#removendo items

thisdict.pop("faculdade")
print(thisdict)

#removendo o ultimo item do dicionario

thisdict.popitem
print(thisdict)

#utilizando o metodo del, o metodo del remove um item com o nome de chave especificado

#del thisdict["estudante"]
#print(thisdict)


#limpando o dicionario(excluindo todos os itens)
#thisdict.clear()
#print(thisdict)





#copia do dicionario utilizando o metodo dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#dicionarios aninhados

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

#Dicionario que contém os outros 3 dicionários-
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#utilizando o dict para criar um dicionario

thisdict2 = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict2)
