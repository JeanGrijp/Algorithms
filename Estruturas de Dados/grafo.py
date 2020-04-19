"""
Copyright: GRIJP, Jean.
(06/2019)

"""
class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.visitado = False


class Aresta:
	def __init__(self, origem, destino, peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso


class Grafo:
    def __init__(self, direcionado = False):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado

    def inserir_vertice(self, valor):
        flag = False
        for i in self.lista_Vertices:
            if i.valor == valor:
                flag = True
        if len(self.lista_Vertices) == 0:
            self.lista_Vertices.append(Vertice(int(valor)))
        elif flag:
            print("Vertice já inserido")
        else:
            self.lista_Vertices.append(Vertice(int(valor)))

    def inserir_aresta(self, origem, destino, peso):
        origem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um dos Vertices ou ambos não existem")
        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))

    def busca_vertice(self, identificador):
        for i in self.lista_Vertices:
            if identificador == i.valor:
                return i
        return None

    def busca_aresta(self, inicio, final):
        for aresta in self.lista_Arestas:
            origem = aresta.origem
            destino = aresta.destino
            if origem.valor == inicio.valor and destino.valor == final.valor:
                return aresta
        return None

    def busca_adjacente(self, vertice):
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].origem
            destino = self.lista_Arestas[i].destino
            if (vertice.valor == origem.valor) and (destino.visitado == False):
                destino.visitado = True
                return destino
        else:
            return None

    def inicializador(self, vertice):
        for v in self.lista_Vertices:
            v.visitado = False
        vertice.visitado = True

    def vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def menor_aresta(self, x, lista):
        menor = None
        menor_peso = None
        for i in lista:
            if i.origem.valor == x.valor and i.destino.visitado == False:
                if menor_peso is None:
                    menor = i
                    menor_peso = i.peso
                else:
                    if i.peso < menor_peso:
                        menor = i
                        menor_peso = i.peso
        print(type(menor))
        menor.origem.visitado = True
        return menor

    def arvore_geradora_minima(self, num):
        print("Iniciou")
        arvore = []
        font = busca_vertice(num)
        if font is None:
            print("Vertice não encontrado")
            return
        cont = 0
        x = font
        while len(self.lista_Vertices) > cont:
            if x.visitado == False:
                y = self.menor_aresta(x, self.lista_Arestas)
                arvore.append(y)
                cont += 1
                x = y.destino
        string = ""
        for i in arvore:
            string += "{} -> {};".format(i.origem, i.destino)
        return string


grafo = Grafo()
num = int(input("Digite a quantidade de vertice que quer inserir: "))
for i in range(num):
    num2 = int(input("Digite o valor do vertice: "))
    grafo.inserir_vertice(num2)


num = int(input("Digite a quantidade de arestas que deseja formar: "))
for i in range(num):
    num2 = int(input("Digite o valor do vertice 1: "))
    flag = False
    for j in grafo.lista_Vertices:
        if j.valor == num2:
            flag = True
    if flag:
        num3 = int(input("Digite o valor do vertice 2: "))
        aux = False
        for j in grafo.lista_Vertices:
            if j.valor == num3:
                aux = True
        if aux:
            peso = int(input("Digite o peso: "))
            grafo.inserir_aresta(num2, num3, peso)
            print("Aresta criada")
        else:
            print("Vertice não encontrado")
            break
    else:
        print("Vertice não encontrado")
        break
x = int(input("Digite o valor do vertice, por onde deseja começar a árvore: "))
print(grafo.arvore_geradora_minima(grafo.lista_Vertices[x]))



