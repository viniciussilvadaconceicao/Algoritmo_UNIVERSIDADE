'''Counting Sort ordena contando ocorrências de valores. É ideal quando a faixa de valores é pequena comparada ao tamanho da lista,
 permitindo posicionar cada elemento corretamente.'''

def counting_Sort(lista):
    m = max(lista) + 1
    count = [0] * m                
    
    for a in lista:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            lista[i] = a
            i += 1
    return lista

if __name__ == "__main__":
    lista = [21, 11, 8, 97, 1, 21, 0, 9, 22, 3]
    print(f"Lista original:{lista}")
    counting_Sort(lista)
    print("Lista ordenada:", lista)