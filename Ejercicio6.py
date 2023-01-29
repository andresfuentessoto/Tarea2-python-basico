"""
Se crea una lista aleatoria
se crea una variable lista2
donde entra a un for con i se da un largo de lista de la lista aleatoria
y se va agregando lo que esta en lista 1 que no esta en lista 2
y se imprime la lista 2, sin repetidos ya que unicamente se agrega lo que esta en lista 1
que no esta en lista 2
"""

Lista1 = [1,3,2,4,7,3,2,2,1,4,10,5,5,10,36,36]
Lista2 = []
for i in range(len(Lista1)):
    if Lista1[i] not in Lista2:
        Lista2.append(Lista1[i])
print (Lista2)        