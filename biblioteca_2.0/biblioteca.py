from os import system, name
from stdiomask import getpass
from time import sleep
from adm import usuario_adm, senha_adm

'''Função para exibir o menu'''
def menu():
    print("-="*35)
    print("""Bem-vindo à biblioteca virtual. Escolha uma opção:
          
          [1] Fazer login
          [2] Fazer cadastro
          [3] Sair
          
          """)
    print("-="*35)
    while True:
        try:
            opcao = int(input('Digite sua opção: '))
            return opcao
        except ValueError:
            print("Opção inválida! Por favor, digite um número correspondente à sua opção.")

'''Função para cadastrar livro'''
def cadastrar_livro():
    livro = input("Digite o nome do livro: ")
    while True:
        try:
            quant_livros = int(input("Digite a quantidade de exemplares disponíveis: "))
            if quant_livros <= 0:
                print("A quantidade deve ser um número positivo maior que zero.")
            else:
                break
        except ValueError:
            print("Quantidade inválida! Por favor, digite um número inteiro.")

    try:
        with open('livros.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(f'{livro},{quant_livros}\n')
        print(f'O livro "{livro}" foi cadastrado com sucesso com {quant_livros} exemplar(es) disponível(eis).')
        sleep(2)
    except Exception as e:
        print(f'Erro ao cadastrar livro: {e}')

'''Função para exibir as opções de livros disponíveis para o usuário'''
def opcoes_usuario():
    try:
        with open('livros.txt', 'r', encoding='utf-8') as arquivo:
            livros = arquivo.readlines()
            print("-="*35)
            print("Livros disponíveis para reserva:")
            for i, livro_info in enumerate(livros, start=1):
                livro, quantidade = livro_info.strip().split(',')
                print(f"[{i}] {livro}")
    except FileNotFoundError:
        print("Não há livros cadastrados no momento.")

'''Função para exibir o menu do administrador'''
def menu_administrador():
    print("""Bem-vindo ao painel do administrador. Escolha uma opção:
          
          [1] Cadastrar livro
          [2] Excluir usuário
          [3] Sair
          
          """)
    while True:
        try:
            opcao = int(input('Digite sua opção: '))
            return opcao
        except ValueError:
            print("Opção inválida! Por favor, digite um número correspondente à sua opção.")


        system('cls' if name == 'nt' else 'clear')
        opcao = menu()

        if opcao == 1:
            
            while True:
                print("-="*35)
                login = input('Digite seu nome de usuário: ')
                senha = getpass(prompt='Senha: ', mask='*')
                print("-="*35)
                if login == usuario_adm and senha == senha_adm:
                    print('Login de administrador APROVADO!')
                    sleep(2)
                    while True:
                        system('cls' if name == 'nt' else 'clear')
                        opcao_admin = menu_administrador()

                        if opcao_admin == 1:
                            cadastrar_livro()
                        
                        elif opcao_admin == 2:
                            # Chamar função para excluir usuário
                            pass
                        elif opcao_admin == 3:
                            print("Retornando ao menu principal...")
                            sleep(2)
                            break
                        else:
                            print("Opção inválida! Tente novamente.")
                            sleep(2)
                    break
                else:
                    user_exists = busca_usuario(login, senha)
                    if user_exists:
                        print('Login APROVADO!')
                        sleep(2)
                        break
                    else:
                        print('ERRO, tente novamente')
                        sleep(2)

        elif opcao == 2:
            system('cls' if name == 'nt' else 'clear')
            cadastrar_usuario()

        elif opcao == 3:
            system('cls' if name == 'nt' else 'clear')
            print("Tchau...")
            sleep(2)
            break

        else:
            print("Opção inválida! Tente novamente.")
            sleep(2)

'''Função para buscar um usuário no arquivo de usuários.txt'''
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

'''Função para verificar se um nome de usuário existe'''
def usuario_existe(login):
    try:
        with open('usuarios.txt', 'r', encoding='utf-8', newline='') as arquivo:
            for linha in arquivo:
                parts = linha.strip().split()
                if len(parts) == 2:
                    nome, _ = parts
                    if nome == login:
                        return True
    except FileNotFoundError:
        return False
    return False

'''Função para cadastra um novo usuário no arquivo de usuários.txt'''
def cadastrar_usuario():
    while True:
        print("-="*35)
        login = input('Digite o login desajado: ')
        if usuario_existe(login):
            print("Usuário já existe! Por favor, escolha outro login...")
            sleep(2)
            continue
        else:
            senha = getpass(prompt='Digite a senha desejada: ', mask='*')
            confirmar_senha = getpass(prompt='Confirme a senha: ', mask='*')
            print("-="*35)

        if senha != confirmar_senha:
            print('As senhas não coincidem. Tente novamente.')
            sleep(2)
            continue

        try:
            with open('usuarios.txt', 'a', encoding='utf-8', newline='') as arquivo:
                arquivo.write(f'{login} {senha}\n')
            print('Usuário cadastrado com sucesso!')
            sleep(2)
            break
        except Exception as e:
            print(f'Erro ao cadastrar usuário: {e}')
            sleep(2)
            continue


    system('cls' if name == 'nt' else 'clear')
    opcao = menu()

    if opcao == 1:
        while True:
            print("-="*35)
            login = input('Digite seu nome de usuário: ')
            senha = getpass(prompt='Senha: ', mask='*')
            print("-="*35)
            user_exists = busca_usuario(login, senha)
            if user_exists:
                print('Login APROVADO!')
                sleep(2)
                break
            else:
                print('ERRO, tente novamente')
                sleep(2)

    elif opcao == 2:
        system('cls' if name == 'nt' else 'clear')
        cadastrar_usuario()

    elif opcao == 3:
        system('cls' if name == 'nt' else 'clear')
        print("Tchau...")
        sleep(2)
       

    else:
        print("Opção inválida! Tente novamente.")
        sleep(2)

'''Loop principal'''
while True:
    system('cls' if name == 'nt' else 'clear')
    opcao = menu()

    if opcao == 1:
        while True:
            print("-="*35)
            login = input('Digite seu nome de usuário: ')
            senha = getpass(prompt='Senha: ', mask='*')
            print("-="*35)
            if login == usuario_adm and senha == senha_adm:
                print('Login de administrador APROVADO!')
                sleep(2)
                while True:
                    system('cls' if name == 'nt' else 'clear')
                    opcao_admin = menu_administrador()

                    if opcao_admin == 1:
                        cadastrar_livro()
                      
                    elif opcao_admin == 2:
                        ''' Chamar função para excluir usuário'''
                        pass
                    elif opcao_admin == 3:
                        print("Retornando ao menu principal...")
                        sleep(2)
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
                        sleep(2)
                break
            else:
                user_exists = busca_usuario(login, senha)
                if user_exists:
                    print('Login APROVADO!')
                    sleep(2)
                    while True:
                        system('cls' if name == 'nt' else 'clear')
                        opcoes_usuario()
                        print("[0] retornar")
                        print("-="*35)
                        opcao_reserva = input("Digite o número do livro que deseja reservar: ")
                        if opcao_reserva == '0':
                            print("Retornando ao menu principal...")
                            sleep(2)
                            system('cls' if name == 'nt' else 'clear') 
                            opcao = menu()  
                            break  
                       
                        try:
                            opcao_reserva = int(opcao_reserva)
                            with open('livros.txt', 'r', encoding='utf-8') as arquivo:
                                livros = arquivo.readlines()
                                if 0 < opcao_reserva <= len(livros):
                                    livro_reservado = livros[opcao_reserva - 1].strip().split(',')[0]
                                    print(f"Você reservou o livro '{livro_reservado}'.")
                                    sleep(2)
                                   
                                else:
                                    print("Opção inválida! Por favor, digite um número correspondente a um livro da lista.")
                                    sleep(2)
                        except ValueError:
                            print("Opção inválida! Por favor, digite um número correspondente a um livro da lista.")
                            sleep(2)
                else:
                    print('ERRO, tente novamente')
                    sleep(2)


    elif opcao == 2:
        system('cls' if name == 'nt' else 'clear')
        cadastrar_usuario()

    elif opcao == 3:
        system('cls' if name == 'nt' else 'clear')
        print("Tchau...")
        sleep(2)
        break 

    else:
        print("Opção inválida! Tente novamente.")
        sleep(2)
