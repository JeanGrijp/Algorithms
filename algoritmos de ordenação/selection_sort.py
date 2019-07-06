import random
import time
import sys
sys.setrecursionlimit(1000000000) #aumenta o valor da pilha recursiva na memoria.


def selection_sort(vetor, indice):
	if indice >= len(vetor)-1:
		return -1
	minIndice = indice # minIndice vai guardar posicao onde esta o menor valor em relacao ao indice
	for x in range(indice+1, len(vetor)):
		if vetor[x] < vetor[minIndice]:
			minIndice = x
	temp = vetor[indice]
	vetor[indice] = vetor[minIndice]
	vetor[minIndice] = temp
	selection_sort(vetor, indice+1)
	return vetor



lista = []
for i in range(1000, 0, -1):
    lista.append(i)
tempo1 = time.time_ns()
selection_sort(lista, 0)
tempo2 = time.time_ns()
tempo = (tempo2 - tempo1) / 1000000
print("Tempo: %i ms"%tempo)
