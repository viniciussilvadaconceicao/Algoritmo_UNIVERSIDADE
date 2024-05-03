'''Escreva uma função que receba uma lista ordenada como parâmetro e
retorne uma nova lista contendo apenas os números ímpares, e outra lista
com os números pares da lista original.
Considere: Lista [1,2,3, ... , 10000] '''

def lista_ordenada(lista):

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)

        else:
            impares.append(numero)
    return impares, pares

lista_original = list(range(1, 10001))
impares, pares = lista_ordenada(lista_original)


print(f'''Números ímpares:{impares}
      
Números pares: {pares}''')

