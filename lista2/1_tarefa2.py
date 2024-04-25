'''1. As Organizações PythonMaster resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5%
o Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o
percentual de aumento aplicado; o valor do aumento; o novo salário, após o
aumento'''

salario = float(input('digite o valor do salário de um colaborador R$:'))

if salario <= 280:
    aumen = salario * 20 / 100 
    novo_sal = aumen + salario
    print('\n')
    print(f'''Salario antes do reajuste: {salario}R$  
Percentual de aumento aplicado: 20% 
Valor do aumento: {aumen:.1f}R$
Novo salário após o aumento: {novo_sal:.1f}R$''')
    print('\n')

elif salario <= 700:
    aumen = salario * 15 / 100 
    novo_sal = aumen + salario
    print('\n')
    print(f'''Salario antes do reajuste: {salario}R$  
Percentual de aumento aplicado: 15% 
Valor do aumento: {aumen:.1f}R$
Novo salário após o aumento: {novo_sal:.1f}R$''')
    print('\n')

elif salario <= 1500:
    aumen = salario * 10 / 100 
    novo_sal = aumen + salario
    print('\n')
    print(f'''Salario antes do reajuste: {salario}R$  
Percentual de aumento aplicado: 10% 
Valor do aumento: {aumen:.1f}R$
Novo salário após o aumento: {novo_sal:.1f}R$''')
    print('\n')

else:
    aumen = salario * 5 / 100 
    novo_sal = aumen + salario
    print('\n')
    print(f'''Salario antes do reajuste: {salario}R$  
Percentual de aumento aplicado: 5% 
Valor do aumento: {aumen:.1f}R$
Novo salário após o aumento: {novo_sal:.1f}R$''')
    print('\n')