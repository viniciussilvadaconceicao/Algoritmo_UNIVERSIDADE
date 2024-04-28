'''2. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

• Desconto do IR:
• Salário Bruto até 900 (inclusive) - isento
• Salário Bruto até 1500 (inclusive) - desconto de 5%
• Salário Bruto até 2500 (inclusive) - desconto de 10%
• Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. 

No exemplo o valor da hora é 5 e aquantidade de hora é 220.
 Salário Bruto: (5 * 220) : R$ 1100,00
 (-) IR (5%) : R$ 55,00
 (-) INSS ( 10%) : R$ 110,00
 FGTS (11%) : R$ 121,00
 Total de descontos : R$ 165,00
 Salário Liquido : R$ 935,00'''

hrs = float(input('Qual o valor da sua hora trabalhada:'))
print('\n')
hrs_mes = float(input('Quantas horas você trabalha no mês:'))
print('\n')
salario = hrs * hrs_mes

if salario <= 900:
    inss = salario * 10 / 100 
    fgts = salario * 11 / 100
    sal_liq = salario - inss
    print(f'''Salário bruto: ({hrs} * {hrs_mes})           :R${salario:.2f}
(-)IR                                  :(isento)
(-)INSS(10%)                           :R${inss:.2f}
FGTS(11%)                              :R${fgts:.2f}
Total de desconto                      :R${inss:.2f}
Salario liquido                        :R${sal_liq:.2f}''')
    print('\n')

elif salario <= 1500:
   ir = salario * 5 / 100
   inss = salario * 10 / 100
   fgts = salario * 11 / 100 
   desconto =  ir + inss
   sal_liq = salario - ir - inss
   print(f'''Salário bruto: ({hrs} * {hrs_mes})          :R${salario:.2f}
(-)IR(5%)                              :R${ir:.2f}
(-)INSS(10%)                           :R${inss:.2f}
FGTS(11%)                              :R${fgts:.2f}
Total de desconto                      :R${desconto:.2f}
Salario liquido                        :R${sal_liq:.2f}''')
   print('\n')

elif salario <= 2500:
    ir = salario * 10 / 100 
    inss = salario * 10 / 100
    fgts = salario * 11 / 100
    desconto = ir + inss
    sal_liq = salario - desconto
    print(f'''Salário bruto: ({hrs} * {hrs_mes})          :R${salario:.2f}
(-)IR(10%)                             :R${ir:.2f}
(-)INSS(10%)                           :R${inss:.2f}
FGTS(11%)                              :R${fgts:.2f}
Total de desconto                      :R${desconto:.2f}
Salario liquido                        :R${sal_liq:.2f}''')
    print('\n')

else:
    ir = salario * 20 / 100
    inss = salario * 10 / 100
    fgts = salario * 11 / 100
    desconto = ir + inss
    sal_liq = salario - inss - ir
    print(f'''Salário bruto: ({hrs} * {hrs_mes})          :R${salario:.2f}
(-)IR(20%)                             :R${ir:.2f}
(-)INSS(10%)                           :R${inss:.2f}
FGTS(11%)                              :R${fgts:.2f}
Total de desconto                      :R${desconto:.2f}
Salario liquido                        :R${sal_liq:.2f}''')
    print('\n')
