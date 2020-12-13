inteiros = [1,3,4,5,7,8]
quadrados = [n*n for n in inteiros]
print(quadrados)


inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0 ]
print(pares)

def soma_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero + segundo_numero)

def subtrai_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero - segundo_numero)

def multiplica_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero * segundo_numero)

def divide_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero / segundo_numero)
