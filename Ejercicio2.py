"""
Se le pide al usuario ingresar un numero mayor a 0
un if por si el numero ingresado es negativo y tire un error con texto
entra a un ciclo for donde imprime el 1
despues se sale y vuelve a entrar para sumarle 1 e imprimir el 1 2
y asi repetidamente hasta que llega al numero ingresado
"""
numero=int(input("Por favor ingrese un número mayor a 0, gracias:")) 
if numero<0:
    print("Error, por favor ingrese un número mayor a 0")
for i in range (1,numero+1):
    for j in range (1, i+1):
         print(j , end=" ")
    print("")    
    