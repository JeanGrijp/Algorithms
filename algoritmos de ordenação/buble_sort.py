import random
import time
import sys
sys.setrecursionlimit(1000000) #aumenta o valor da pilha recursiva na memoria.


def bubble_sort(lista):
		elementos = len(lista)-1
		ordenado = False
		while not ordenado:
			ordenado = True
			for i in range(elementos):
				if lista[i] > lista[i+1]:
					lista[i], lista[i+1] = lista[i+1],lista[i]
					ordenado = False        
		return lista


lista = []
for i in range(10, 0, -1):
    lista.append(i)
#tempo1 = time.time_ns()
print(lista)
bubble_sort(lista)
#tempo2 = time.time_ns()
#tempo = (tempo2 - tempo1) / 1000000
#print("Tempo: %i ms"%tempo)
print(lista)