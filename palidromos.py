#Programa una función que nos devuelva si una palabra o texto es palíndromo (TRUE) o no (FALSE). 
#Una palabra o texto es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.

mi_funcion = 'dabale arroz a la zorra el abad'
rever = mi_funcion[::-1]
if mi_funcion == rever:
    print("La palabra ingresada si es palindromo!")
else:
    print("La palabra ingresada no es palindromo!")


