"""
De una lista definida
imprima la lista
entra a un for con i de variable y va agarrando cada numero de la lista y elevandola al cubo
impimiendo la lista al cubo
"""

lista=[1,2,3,4,5,6,7,]
 
print ("Lista original", lista)
 
for i in range(0,len(lista)):
	lista[i]=lista[i]*lista[i]*lista[i]
 
print ("La lista al cubo es", lista)




