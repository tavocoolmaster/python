from turtle import color


colores=["rojo","azul","negro"]
lista_numeros=list((1,2,3,4))
print(lista_numeros)

#devolver un rango de numeros en una lista
R=list(range(1,11))
print(R)

#devolvemos el valor segun la posicion de su indice
print(colores[2])

#devuelve verdadero o falso si encuentra en la lista
print("Verde" in colores)
print("azul" in colores)

#imprimir la lista colores
print(colores)
#realizar un cambio un elemneto de la lista
colores[1]="amarillo"
print(colores)
#agregar un nuevo elemento a la lista
colores.append("tomate")
print(colores)

#agregar varios elementos a una lista usando una tupla
colores.extend(("purpura","blanco","rosa"))
print(colores)

#agregar elementos a partir de una posicion
colores.insert(1,"plomo")
print(colores)
#otro ejemplo mas agregando al final de la lista colores
colores.insert(len(colores),"cafe")
print( colores)

#remover elementos de una lista que estan en el indice determinado
colores.pop(2)
print(colores) 

#remover un elemento identificado con su nombre
colores.remove("negro")
print(colores)

#borra todos los elementos de una lista
#colores.clear()
#print(colores)

#ordenar elementos de a -z
colores.sort()
print(colores)
#ordenar de manera inversa de la z-a
colores.sort(reverse=True)
print(colores)

#obtener un indice de un elemento
print(colores.index("tomate"))