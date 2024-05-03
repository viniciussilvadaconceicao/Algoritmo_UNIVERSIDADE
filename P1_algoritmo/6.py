'''6. Crie uma função que lê o ano de nascimento de uma pessoa e o ano atual.
Calcule e mostre qual é: a idade da pessoa em anos, a idade da pessoa
em meses, a idade da pessoa em dias e a idade da pessoa em semanas'''

def calculadora(nasc, atual):
    anos = atual - nasc
    meses = anos * 12
    dias = anos * 365
    semanas = dias // 7

    print(f'''Idade em anos: {anos}
Idade em meses: {meses}
Idade em dias: {dias}
Idade em semanas: {semanas}''')
    
print('\n')
nasc_ano = int(input('Digite o ano de nascimento: '))
at_ano = int(input('Digite o ano atual: '))
print('\n')
calculadora(nasc_ano, at_ano)
print('\n')