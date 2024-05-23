import os
import getpass
import stdiomask
from time import sleep

livros_disponiveis = ["Harry Potter", "O Senhor dos Aneis", "A Culpa e das Estrelas", "O Codigo Da Vinci", "Jogos Vorazes", "Cinquenta Tons de Cinza"]
usuario_reserva = {}


# Função para exibir o menu
def menu():
    print("""Bem-vindo à biblioteca virtual. Escolha uma opção:
          
          [1] Cadastrar novo usuário
          [2] Fazer login
          [3] Sair
          """)
    while True:
        try:
            opção = int(input('Digite sua opção: '))
            return opção
        except ValueError:
            print("Opção inválida! Por favor, digite um número correspondente à sua opção.")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    login = input('Digite seu nome de usuário: ')
    senha = stdiomask.getpass(prompt='Senha:', mask='*')
    return login, senha

# Função para buscar um usuário no arquivo de usuários
def busca_usuario(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r', encoding='utf-8', newline='') as arquivo:
            for linha in arquivo:
                parts = linha.strip().split()
                if len(parts) == 2:
                    nome, password = parts
                    usuarios.append((nome, password))
                else:
                    print(f"Erro no formato da linha: {linha}")
            for nome, password in usuarios:
                if nome == login and password == senha:
                    return True
    except FileNotFoundError:
        return False
    return False

# Exibir livros disponíveis
def livros_exibidos():
    print("Escolha uma opção para escolher o livro desejado:")
    print('\n')
    for i ,livro in enumerate(livros_disponiveis):
        print(f"[{i}] {livro}")
    print()
    while True:
        try:
            opcao_livro = int(input('Digite sua opção em números: '))
            if opcao_livro in range(len(livros_disponiveis)):
                return opcao_livro
            else:
                print("Opção inválida! Escolha uma opção de 0 a", len(livros_disponiveis) - 1)
        except ValueError:
            print("Opção inválida! Por favor, digite um número correspondente à sua opção.")
# Função para armazenar reserva
def armazenar_rezerva(login, livro):
    livro_escolhido = livros_disponiveis[livro]
    if login in usuario_reserva:
        usuario_reserva[login].append(livro_escolhido)
    else:
        usuario_reserva[login] = [livro_escolhido]
    with open('reservas.txt', 'a') as arquivo:
        arquivo.write(f"{login}:{livro_escolhido}\n")

def new_func(opcao_livro):
    return opcao_livro
       
# Função para exibir as reservas dos usuários
def exibir_reservas():
    print("\nReservas dos usuários:")
    for usuario, reservas in usuario_reserva.items():
        print(f"{usuario}: {', '.join(reservas)}")
    print()

# Função para ler as reservas dos usuários a partir do arquivo
def ler_reservas():
    if os.path.exists('reservas.txt'):
        with open('reservas.txt', 'r') as arquivo:
            for linha in arquivo:
                login, livro_reservado = linha.strip().split(':')
                armazenar_rezerva(login, livro_reservado)

# Função para devolver um livro
def devolver_livro(login):
    if login in usuario_reserva and usuario_reserva[login]:
        livro_devolvido = usuario_reserva[login].pop()
        livros_disponiveis.append(livro_devolvido)
        # Remover a reserva do arquivo de reservas
        with open('reservas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('reservas.txt', 'w') as arquivo:
            for linha in linhas:
                if not linha.startswith(f"{login}:{livro_devolvido}"):
                    arquivo.write(linha)
        print(f"O livro '{livro_devolvido}' foi devolvido com sucesso.")
    else:
        print("Você não tem nenhum livro reservado no momento.")

# Loop principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    opção = menu()

    if opção == 1:
        login, senha = cadastrar_usuario()
        if login == senha:
            print("Login deve ser diferente da senha.")
            sleep(2)
            continue 
        user_exists = busca_usuario(login, senha)
        if user_exists:
            print("Usuário já existe!")
            sleep(2)
            continue 
        else:
            with open('usuarios.txt', 'a+', encoding='utf-8', newline='') as arquivo:
                arquivo.write(f"{login} {senha}\n")
                print('Cadastro APROVADO!')
                sleep(2)
    
    elif opção == 2:
        login, senha = cadastrar_usuario()
        user_exists = busca_usuario(login, senha)
        if user_exists:
            print('Login APROVADO!')
            sleep(2)
            if login in usuario_reserva and usuario_reserva[login]:
                print("[4] Devolver livro")
            while True:
                livros_exibidos()
                opcao_livro = int(input("Digite o número do livro que deseja reservar: "))
                if opcao_livro in range(len(livros_disponiveis)):
                    armazenar_rezerva(login, opcao_livro)
                    print("Livro reservado com sucesso!")
                    sleep(2)
                    break
        else:
            print('Você deve ter digitado seu nome de usuário ou senha errado')
    
    
    elif opção == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tchau...")
        sleep(2)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
        sleep(2)
