import random
import time


def insertion_sort(vetor):
	for x in range(1, len(vetor)):
		referencia = vetor[x]
		aux = x-1
		while aux >= 0 and vetor[aux] > referencia:#
			vetor[aux+1] = vetor[aux]
			aux -= 1
		vetor[aux+1] = referencia
	return vetor


lista = []
for i in range(1000, 0, -1):
    lista.append(i)
tempo1 = time.time_ns()
insertion_sort(lista)
tempo2 = time.time_ns()
tempo = (tempo2 - tempo1) / 1000000
print("Tempo: %i ms"%tempo)
