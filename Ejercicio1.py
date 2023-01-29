"""
Se le pide al usuario ingresar un numero entero
se ponen condiciones para que si el usuario ingresa un numero negativo de error
si el numero es entero entra en un for par que vaya realizando el factorial del numero ingresado
despues que lo imprima
"""


numero=int(input("Por favor ingrese un número entero"))
factorial=1
if numero<0:
        print("Error número negativo, por favor ingrese un número entero")
if numero>=0:
    for i in range(1,numero+1):    
        factorial=factorial*i       
print("Factorial:",factorial) 





