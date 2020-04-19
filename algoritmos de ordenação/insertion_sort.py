def insertion_sort(vetor):
	for x in range(1, len(vetor)):
		referencia = vetor[x]
		aux = x-1
		while aux >= 0 and vetor[aux] > referencia:#
			vetor[aux+1] = vetor[aux]
			aux -= 1
		vetor[aux+1] = referencia
	return vetor
