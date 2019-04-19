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
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = No(None)

    
    def inserir(self, valor):
        if self.inicio.valor is None: #verifica se a fila está vazia, caso esteja, o primeiro elemento da fila será o valor.
            self.inicio = No(valor)
        else:#caso não esteja vazia
            aux = self.inicio #cria-se uma variavel auxiliar para percorrer a fila e encontrar o final da fila.
            while aux.proximo is not None: #enquanto não encontrar o ultimo elemento, o while faz com que a variavel aux seja o proximo elemento da fila
                aux = aux.proximo
            aux.proximo = No(valor) #quando chegar no ultimo elemento, sai do while e o valor é inserido ao final da fila.


    def remover(self):
        if self.inicio.valor is None: #verifica se a fila está vazia
            return None
        else:
            aux = self.inicio #cria-se uma variavel auxiliar
            if self.inicio.proximo is None: #verifica se a fila tem apenas um elemento
                self.inicio = No(None) #se tiver apenas um elemento, a fila volta a ficar vazia.
            else:
                self.inicio = aux.proximo #caso tenha mais de um elemento, é removido o primeiro elemento.

    
    def mostrar(self):
        if self.inicio.valor is None: #verifica se a fila está vazia
            print("Fila vazia")
        else:
            aux = self.inicio #cria-se a variavel auxiliar
            while aux.proximo is not None: #o while faz printar os valores dos objetos inseridos na fila
                print(aux.valor)
                aux = aux.proximo