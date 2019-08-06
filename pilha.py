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

class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = No(None) #o primiero objeto é um sentinela, ele não conta como objeto inserido, a pilha inicia com o sentinela para ter a noção do inicio e o fim da pilha.

    def insert(self, value):
        """
        esse metrodo recebe como parâmetro um valor, e por se tratar de uma pilha
        ele insere o valor no final da pilha.
        """
        if self.first.value is None: #verifica se a pilha está vazia, caso esteja, o primeiro elemento recebe um objeto do tipo No() com o valor.
            self.first = No(value)
        else:
            aux = self.first #essa variavel guarda a referência do inicio da pilha 
            while aux.next is not None: #enquanto não chegar no ultimo elemento da pilha, ele vai procurando
                aux = aux.next
            aux.next = No(value) #quando chega no ultimo elemento da pilha, ele coloca o valor passado no parâmetro como o ultimo objeto.
    
    def remove(self):
        if self.first.value is None: #se a pilha estiver vazia, não tem nenhum elemento a ser removido
            print("Pilha vazia")
        else:
            aux = self.first #aux é uma variavel que guarda a referencia do primeiro objeto da pilha
            aux_before = aux #para cada vez que a variavel aux avançar dentro do while, a aux_before guarda a referencia do objeto anterior, para quando a aux encontrar o ultimo objeto, a aux_before.next ser None, assim removendo o ultimo elemento da pilha.
            while aux.next is not None: #enquanto esse objeto não foi o ultimo, ele vai procurando até encontrar
                aux_before = aux
                aux = aux.next
            aux_before.next = None #removendo o ultimo elemento, deixando de referencia-lo.

    def show(self):
        if self.first.value is None:
            print("Pilha vazia")
        else:
            aux = self.first
            while aux.next is not None:
                print(aux.value)
                aux = aux.next

