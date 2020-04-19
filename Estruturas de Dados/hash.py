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


esse cósigo é uma resolução do paradoxo do aniversário, onde é verificado se duas pessoas fazem aniversário no mesmo dia, se sim, é mostrado os nomes das pessoas,
caso contrário, a mensagem de que ninguem faz aniversário no mesmo dia é mostrada.

"""


class No:
    def __init__(self, nome = None, dia = None, mes = None):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.proximo = None



class Tabela_hash:
    def __init__(self):
        self.tabela = [None] * 366
        self.meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        self.dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    def inserir(self, chave, nome, dia, mes):
        if self.tabela[chave] is None:
            self.tabela[chave] = No(nome, dia, mes)
        else:
            aux = self.tabela[chave]
            anterior = aux
            while aux is not None:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = No(nome, dia, mes)


    def buscar(self, chave):
        lista = []
        if self.tabela[chave] is None:
            return None
        else:
            if self.tabela[chave].proximo is not None:
                lista.append(self.tabela[chave].nome)
                aux = self.tabela[chave].proximo
                while aux is not None:
                    lista.append(aux.nome)
                    aux = aux.proximo
            else:
                return None
        num = int(self.tabela[chave].mes)
        string = ("Dia {} de {}: ".format((self.tabela[chave].dia), self.meses[num - 1]))
        lista.append('&&&')
        for i in lista:
            if i != '&&&':
                string += str(i)
                string += ','
                string += " "
        string = string[:len(string)-2]
        return string


def verifica():
    hashing = Tabela_hash()
    print("Padrão a ser obedecido ao passar os nomes dos aniversariantes: nome dia mes")
    num2 = int(input("Digite a quantidade de aniversariantes: "))
    for i in range(num2):
        pessoa = input("Digite o nome da pessoa e a data de aniversário: ")
        string = pessoa.split(" ")
        nome = string[0]
        dia = int(string[1])
        mes = int(string[2])
        aux = 0
        for i in range(mes-1):
            aux += hashing.dias[i]
        chave = dia + aux
        hashing.inserir(chave, nome, dia , mes)
    final = []
    for i in range(len(hashing.tabela)):
        aux = hashing.buscar(i)
        if aux is not None:
            final.append(aux)

    if len(final) > 0:
        for i in final:
            print(i)
    else:
        print("Ninguem faz aniversario no mesmo dia")
