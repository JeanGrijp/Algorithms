def trocar(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

def particionar(array, begin, end):
    pivo = array[begin] #declara-se um pivo para referencia da ordenação
    while True:
        while array[begin] < pivo:#percorrer o begin array até encontrar um valor maior que o pivo
            begin = begin + 1
        while array[end] > pivo:#percorre do end ao begin da array ate encontrar um valor menor que o pivo
            end = end - 1
        if begin >= end:
            return end
        trocar(array, begin, end)#como o valor do begin é igual ou maior que o pivo, e o end é menor ou igual ao pivo, ocorre a troca
        begin = begin + 1
        end = end - 1

def quick_sort(array, begin, end):
    if begin < end:
        aux = particionar(array, begin, end)# aqui o valor de retorno está na posição certa, então chama-se a função para ambas as partes restantes da array.
        quick_sort(array, begin, aux)
        quick_sort(array, aux+1, end)