#3.O professor Bill Gates está com problemas na gestão de suas classes, e ele não consegue
#corrigir e entregar as notas de seus alunos a tempo. Elon Musk, um de seus alunos decidiu
#ajudá-lo criando um programa para resolver esse problema, porém ele não sabe
#programar, assim pediu sua ajuda para essa tarefa! Crie uma função que recebe um vetor
#de respostas do aluno e um gabarito(questões de múltipla escolha de A até E), que
#retorne a nota do aluno de 0 a 10.


def calcular_nota(respostas_aluno, gabarito):
    nota = 0
    for resposta_aluno, resposta_correta in zip(respostas_aluno, gabarito):
        if resposta_aluno == resposta_correta:
            nota += 1 
    
   
    nota_final = (nota / len(gabarito)) * 10
    return nota_final


respostas_aluno = ['A', 'B', 'C', 'D', 'E']  
gabarito = ['A', 'B', 'C', 'D', 'E'] 
nota_final = calcular_nota(respostas_aluno, gabarito)
print(f"A nota do aluno é: {nota_final:.2f}")
      
      
def calcular_nota(respostas_aluno, gabarito):
    nota = 0
    for resposta_aluno, resposta_correta in zip(respostas_aluno, gabarito):
        if resposta_aluno == resposta_correta:
            nota += 1  
    
    nota_final = (nota / len(gabarito)) * 10
    return nota_final

gabarito = ['A', 'A', 'B', 'D', 'E', 'A', 'C', 'C', 'A', 'D']

respostas_alunos = []

for i in range(3):
    respostas = input(f"Informe as respostas da prova do aluno {i+1} (10 respostas separadas por espaços): ").split()
    respostas_alunos.append(respostas)


print("\nNotas dos alunos:")
for i, respostas_aluno in enumerate(respostas_alunos):
    nota_final = calcular_nota(respostas_aluno, gabarito)
    print(f"Aluno {i+1}: {nota_final:.2f}")