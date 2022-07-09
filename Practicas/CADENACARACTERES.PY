myStr="hello world"
#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello","bye"))
print(myStr.count(" "))
print(myStr.startswith("he"))
print(myStr.endswith("orld"))
print(myStr.endswith("orld"))
#divide una cadena de caracteres en varias partes separadas por espacios o un caracter determinado
print(myStr.split())
#busca la posicion de las letra buscada
print(myStr.find("w"))
#cuenta el numero de caracteres
print(len(myStr))
#busca el indice de una palabra
print(myStr.index("e"))
#comprueba si es numerico
print(myStr.isnumeric())
#comprueba si es alfanumerico
print(myStr.isalpha())

#devuelve el caracter segun la posicion de su indice
print(myStr[0])
print(myStr[-2])

#varias formas de concatenar
print("El mensaje es :"+ myStr )
print(f"El mensaje es : {myStr}" )
print("El mensaje es : {0}".format(myStr))