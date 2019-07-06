import random
import time
import sys
sys.setrecursionlimit(1000000)

"""
MIT License

Copyright (c) 2019 Jean Grijp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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


lista = []
for i in range(0, 100):
    lista.append(random.randint(0, 100))
tempo1 = time.time()
print(lista)
merge_sort(lista)
tempo2 = time.time()
tempo = (tempo2 - tempo1) * 1000
print(lista)

print("Tempo: {} ms".format(tempo))