def selectionSort(vector, index):
	if index >= len(vector)-1:
		return -1
	minIndice = index # minIndice vai guardar posicao onde esta o menor valor em relacao ao index
	for x in range(index+1, len(vector)):
		if vector[x] < vector[minIndice]:
			minIndice = x
	temp = vector[index]
	vector[index] = vector[minIndice]
	vector[minIndice] = temp
	selectionSort(vector, index+1)
	return vector