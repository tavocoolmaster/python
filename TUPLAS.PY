x=(1,2,3)
print(type(x))
meses=("enero","febrero","marzo")

#creando una tupla usando un constructor usando una lista
y=tuple((1,2,3,4))
#dir nos permite sacar los metodos que permite esa clase
print(dir(tuple))
print(y)

#extraer el valor de la tupla segun su indice
print(x[1])

#eliminar la tupla
del x
print(x)
