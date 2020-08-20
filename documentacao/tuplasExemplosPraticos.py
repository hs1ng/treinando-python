thistuple = (1,2,3)
print(thistuple)

print(thistuple[1])


#alterar os valores da tupla

x = list(thistuple)
x[2] = "alterando valor"
thistuple = tuple(x)
print(thistuple)



#loop numa tupla
for x in thistuple:
    print(x)
    
    
    ##verificar se existe
if 4 in thistuple:
    print("O valor 4 existe")
else:
    print("O valor 4 não existe!")
    
#tamanho da tupla

print(len(thistuple))

#tupla com um item, adicione uma virgula

thistuple2 = (2, )
print(thistuple2)


#juntar duas tuplas
thistuple3 = thistuple + thistuple2
print(thistuple3)

#criar uma tupla

thistuple4 = tuple(("sei la", "so sei q nada sei"))
print(thistuple4)