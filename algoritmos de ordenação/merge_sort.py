def merge_sort(x):
    if len(x) == 0 or len(x) == 1: #verifica se a lista está vazia ou se tem apenas um elemento
        return x #caso sim, a lista já está ordenada.
    else:
        metade = int(len(x)/2) #aqui pegamos o tamanho da metade da lista, é importante converter para inteiro, pois uma lista não se adimite indices fracionados.
        metade1 = merge_sort(x[:metade]) #chamo a função recursivamente para a primeira metade da lista
        metade2 = merge_sort(x[metade:]) #chamo a função recursivamente para a segunda metade da lista
        return merge(metade1, metade2) 


def merge(metade1,metade2):
    resultado = [] #cria-se uma lista que conterá todos os elementos das duas listas passadas como parametros de forma ordenada.
    while len(metade1) != 0 and len(metade2) != 0: #enquanto as listas passadas, não ficarem vazias, é porque ainda tem elemento para verificar e ordenar.
        if metade1[0] < metade2[0]: 
            resultado.append(metade1[0]) #adiciona em resultado, o menor elemento, para que o resultado esteja em ordem crescente.
            metade1.remove(metade1[0]) #apois adicionar em resultado, remove da verificação, para que não seja verificado novamente.
        else:
            resultado.append(metade2[0])
            metade2.remove(metade2[0])
    if len(metade1) == 0: 
        resultado += metade2
    else:
        resultado += metade1
    return resultado

