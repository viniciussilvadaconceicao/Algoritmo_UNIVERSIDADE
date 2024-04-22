#2. Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta
#e false caso o contrário. Logo após elabore um “mini-sistema” de checar a senha inserida,
#onde o usuário tem 3 tentativas de senha e caso esse número seja ultrapassado o
#programa é encerrado.

def verificar_senha(senha_correta, senha_inserida):
    return senha_correta == senha_inserida

def mini_sistema():
    senha_correta = "senha123"
    tentativas_restantes = 3
    
    while tentativas_restantes > 0:
        senha_inserida = input("Digite a senha: ")
        
        if verificar_senha(senha_correta, senha_inserida):
            print("Senha correta. Acesso permitido.")
            return True
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(f"Senha incorreta. Você tem mais {tentativas_restantes} tentativa(s) restante(s).")
            else:
                print("Você excedeu o número de tentativas. Acesso negado.")
                return False