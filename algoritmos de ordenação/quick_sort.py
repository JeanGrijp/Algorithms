import random
import time
import sys
sys.setrecursionlimit(10000000) #aumenta o valor da pilha recursiva na memoria.

def trocar(lista, pos1, pos2):
    """
    essa função faz a troca de posição dentro da lista passado
    como parâmetro.
    """
    temp = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = temp

def particionar(lista, inicio, fim):
    pivo = lista[inicio] #declara-se um pivo para referencia da ordenação
    while True:
        while lista[inicio] < pivo:#percorrer o inicio lista até encontrar um valor maior que o pivo
            inicio = inicio + 1
        while lista[fim] > pivo:#percorre do fim ao inicio da lista ate encontrar um valor menor que o pivo
            fim = fim - 1
        if inicio >= fim:
            return fim
        trocar(lista, inicio, fim)#como o valor do inicio é igual ou maior que o pivo, e o fim é menor ou igual ao pivo, ocorre a troca
        inicio = inicio + 1
        fim = fim - 1

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        num = particionar(lista, inicio, fim)# aqui o valor de retorno está na posição certa, então chama-se a função para ambas as partes restantes da lista.
        quick_sort(lista, inicio, num)
        quick_sort(lista, num+1, fim)



lista = []
for i in range(1000, 0, -1): #forma uma lista de mil elementos no pior caso"
    lista.append(i)
tempo1 = time.time_ns()
quick_sort(lista, 0, len(lista)-1)
tempo2 = time.time_ns()
tempo = (tempo2 - tempo1) / 1000000
print("Tempo: %i ms"%tempo)
