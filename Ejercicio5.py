"""
imprime el nombre del estudiante
despues se crea una variable mark list
se buscan los valores de marks y de crea el average de las notas
para luego imprimirlas
"""

sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80,
"math": 90
}
}
}
}

print(sampleDict['class']['student']['name'])
mark_list=[]
for x in sampleDict['class']['student']['marks'].values():
   mark_list.append(x)
average=sum(mark_list)/len(mark_list)
print(average)

