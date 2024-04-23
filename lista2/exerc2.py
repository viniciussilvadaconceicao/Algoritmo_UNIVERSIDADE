'''2. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
um programa que nos dê:

• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• salário líquido.
• calcule os descontos e o salário líquido, conforme a tabela abaixo:'''
import  math
salario_hora = float(input('quanto voçê ganha por hora:'))
horas_mes = float(input('qual o numero de horas trabalhada no mês:'))

salario_mes = salario_hora * horas_mes
salario_mes = math.floor(salario_mes) 
renda = salario_mes * 11 / 100 
inss = renda * 8 / 100
sindicato = salario_mes * 5 / 100 
salario_liquido = salario_mes - renda - inss - sindicato

print(f'''• salário bruto: {salario_mes:.1f}R$
• desconto do INSS: {inss:.1f}R$
• desconto do sindicato: {sindicato:.1f}R$
• salário liquido: {salario_liquido:.1f}R$ ''')
#11.64
#176