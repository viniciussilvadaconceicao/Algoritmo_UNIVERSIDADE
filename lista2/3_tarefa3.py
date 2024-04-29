'''3. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o
exemplo abaixo:
Atleta: Elon Musk
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''


while True:
# usei o while true para quando nã6 digitar nada ele encerrar
    lista = []
    atleta = str(input('qual o nome do atleta:'))
    if atleta == '':
        print('programa encerrado!')
        #break para parar
        break
    n = 5
    soma = 0
    #criei uma variavel para somar entre eles 
    for i in range(n):
        saltos = float(input(f'digite quantos metros do {i+1}° salto:'))
        lista.append(saltos)
        #append para inserir em lista 
        soma = soma + saltos
        media = soma / n
    print(f''''atleta: {atleta}
    teve a media de saltos : {media}m''')