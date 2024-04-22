#1. Crie 2 listas: uma com 5 nomes(João, Maria, Kleber, Caio e Sarah) e outra com 5 valores
#em reais(R$) correspondentes ao saldo da conta do usuário(1350,20; 240,50; 30,00;
#830,15 e 50,00), e usando laços de repetição imprima os dados da seguinte forma(o
#preenchimento das listas deve ser feito também com laços de repetição do mesmo modo
#que será impresso: salvar nome e depois salvar o saldo correspondente):

nomes = []
saldos = []

for i in range(5):
    nome = input("Insira o nome: ")
    nomes.append(nome)
    saldo = float(input("Insira o saldo: "))
    saldos.append(saldo)


print("LISTA DE CLIENTES - BANCO NACIONAL")
print("NOME   SALDO CONTA")
for i in range(5):
    print(f"{nomes[i]}   R${saldos[i]:.2f}   #{i}")