'''2. Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do
outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''

lista = []
n = 0
soma = 0
quantidade = 0
media = 0

while n != -1:
    # se eu inserir somente o n diferente de -1 ele vai entra na lista como uma nota 
    n = float(input(f'digite o valor das notas:'))
    if n != -1:
     #quando digita -1 o programa encerra o loop 
     lista.append(n)
     quantidade = quantidade + 1
     #criei essa variavel para calcular a quantidade de notas inserida 
     soma = soma + n
     #criei essa variavel para somar as notas entre si dentro do loop 
     media = soma / quantidade
     # criei essa variavel para fazer a media das notas inserida que é a soma desses numero dividido pela quantidade de notas
print(f'valores lidos: {lista}')
lista.reverse()
print(f'valores invertidos{lista}')
#inserir a funça reverse para reverter a ordem das notas 
print(f'a soma é {soma}')
print(f'a media é {media}')

media_acima = sum(1 for n in lista if n > media)
#criei esta variavel para contar quantos valores são maior que a media na lista e sua quantidade 
print(f'existe {media_acima} numeros acima da media.')

abaixo_media = sum(1 for n in lista if n < 7 )
#criei essa variavel para contar quantos valores tem abaixo de 7 
print(f'existe {abaixo_media} numeros abaixo de sete.')
print('\n')
print('fim do programa!')