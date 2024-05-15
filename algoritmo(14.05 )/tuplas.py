lista = [1,2,3]
for i in lista():
 print(i)
 print(lista[0])
#tupla ordenada e imutavel
#tupla = (1,2,3)
#tupla = ( 'notabim1', 'notabim2', 'notabima')
#for i in tupla:
 #   print(1)

print("_______")
#set - conjunto - não ordenado , imutável , sem indice
#conjunto = ("a","b","c")

#dict
dicionario = {
    "aluno1" : "nota1",
    "aluno2" : "nota2",
    "aluno3" : "nota3"
}
for i in dicionario:
    print(i)
print("----------")
for chave,valor in dicionario.items():
    print(chave,valor)

print("--------------")
resultado = dicionario.values()
print(resultado)

print("--------------")
listadecompras = ["arroz","feijão","carne"]
for i in listadecompras:
    print(i)
print("--------------")
for indice,elemento in enumerate(listadecompras):
    print(indice,elemento)