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


class Queue:
    def __init__(self):
        self.first = No(None) #o primiero objeto é um sentinela, ele não conta como objeto inserido, a fila inicia com o sentinela para ter a noção do inicio e o fim da fila 

    
    def insert(self, value):
        if self.first.value is None: #verifica se a fila está vazia, caso esteja, o primeiro elemento da fila será o value.
            self.first = No(value)
        else:#caso não esteja vazia
            aux = self.first #cria-se uma variavel auxiliar para percorrer a fila e encontrar o final da fila.
            while aux.next is not None: #enquanto não encontrar o ultimo elemento, o while faz com que a variavel aux seja o next elemento da fila
                aux = aux.next
            aux.next = No(value) #quando chegar no ultimo elemento, sai do while e o value é inserido ao final da fila.


    def remove(self):
        if self.first.value is None: #verifica se a fila está vazia
            return None
        else:
            aux = self.first #cria-se uma variavel auxiliar
            if self.first.next is None: #verifica se a fila tem apenas um elemento
                self.first = No(None) #se tiver apenas um elemento, a fila volta a ficar vazia.
            else:
                self.first = aux.next #caso tenha mais de um elemento, é removido o primeiro elemento.

    
    def show(self):
        if self.first.value is None: #verifica se a fila está vazia
            print("Fila vazia")
        else:
            aux = self.first #cria-se a variavel auxiliar
            while aux.next is not None: #o while faz printar os valuees dos objetos inseridos na fila
                print(aux.value)
                aux = aux.next #enquanto tiver objetos a serem mostrados, aux cntinuará a receber os proximos objetos
