"""faça um algoritmo de busca que:
dada a lista = [20,5,15,24,67,1,45,78,21,11]
se encontrar a chave = 45 retorne a poaição
senão retorne -1 """

def buscasequencial(lista,chave):
 for pos in range(len(lista)):
        if lista[pos] == chave:
            return pos
        return -1

chave = 45
lista = [20,5,15,24,67,1,45,78,21,11]
pos = buscasequencial(lista,chave)

if pos == -1:
    print("não encontrei")

else:
    print("a, chave, ",chave, "esta posição",pos)