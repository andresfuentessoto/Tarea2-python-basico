"""
Se define intercalar que contiene string a y string b
Despues las lineas finales donde se pide le ingreso de la palabra a y b
si no son de la misma cantidad de letras que de error
si lo son continua con las variables r, i y l y entra al while
lo va guardando en string ai y string bi e impriendo intercaladamente
"""

def intercalar(string_a, string_b):

    r = " "
    i = 0
    l = len(a) 

    while i < l:
        print(string_a[i] + string_b[i], end = '')
        i = i + 1
    return r

a = input("Ingrese palabra a: ") 
b = input("Ingrese palabra con misma cantidad de letras que a, palabra b: ")
if len(a)!=len(b):
    print ("Error, por favor ingrese una palabra con la misma cantidad de letras")

else:variables = intercalar(a, b)

print(variables)
