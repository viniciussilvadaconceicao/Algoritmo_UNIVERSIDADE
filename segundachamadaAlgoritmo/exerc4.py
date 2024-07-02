'''faça um programa em python que realize a leitura de 3 notas de um aluno 
o programa deve calcular a média alcançanda por aluno e apresentar:
 a mensagem aprovado se a média for maior ou igual a 7.0
a mensagem reprovado se a média for menor que 7.0
a Aprovação com distinção se a média for igual a 10.0'''

nota = []
soma = 0
cont = 0
for i in range(3):
    num = float(input(f'Digite a {i+1}° nota: '))
    nota.append(num)
    soma += num
    cont += 1
    media = soma / cont
    
if media >= 7:
    print('Aprovado')

elif media < 7:
    print('Reprovado')

elif media == 10:
    print('Aprovado com distincao')