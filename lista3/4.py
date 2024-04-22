
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

while True:
    print("CALCULADORA:")
    print("1- somar")
    print("2- subtrair")
    print("3- multiplicar")
    print("0- sair")

    opcao = input("Insira sua opção: ")

    if opcao == "0":
        print("Até logo!....")
        break
    elif opcao in ["1", "2", "3"]:
        num1 = int(input("Insira o número desejado: "))
        num2 = int(input("Insira o próximo número: "))

        if opcao == "1":
            resultado = somar(num1, num2)
            print("Resultado =", resultado)
        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print("Resultado =", resultado)
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print("Resultado =", resultado)
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

