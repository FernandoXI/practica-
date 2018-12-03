n = []

while len(n) < 2:
    n.append( int ( input ("ingrese un numero: ")))

def menor_valor(arreglo):
    menor = arreglo[0]
    for i in arreglo:
        if i < menor:
            menor= i
    return menor

min = menor_valor(n)
print(n)
print (min)