#Programa una función que reciba como parámetro un array, y que imprima 
# por consola uno a uno sus elementos, diciendo su indice:

mi_funcion = ['hola', 1, True]
for i in range(len(mi_funcion)):
    print("Ocupa el indice [{0}] en el array : {1} ".format(i,mi_funcion[i]))