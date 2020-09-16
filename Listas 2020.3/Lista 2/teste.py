raiz = "raiz"
class Node:
    def __init__(self, dados):
        self.dados = dados
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dados)

class arvoreBinaria:
    def __init__(self, dados=None, node=None):
        if node:
            self.raiz = node
        elif dados:
            node = Node(dados)
            self.raiz = node
        else:
            self.raiz = None

    # Percurso em ordem simétrica 
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            print('(', end='') 
            self.simetric_traversal(node.esquerda)
        print(node, end='')
        if node.direita:
            self.simetric_traversal(node.direita)
            print(')', end='')
    
    def altura(self, node=None):
        if node is None:
            node = self.raiz
        hesquerda = 0
        hdireita = 0
        if node.esquerda:
            hesquerda = self.altura(node.esquerda)
        if node.direita:
            hdireita = self.altura(node.direita)
        if hdireita > hesquerda:
            return hdireita + 1
        return hesquerda + 1

    # Percurso em PÓS ORDEM 
    def posOrdem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.posOrdem(node.esquerda)
        if node.direita:
            self.posOrdem(node.direita)
        print(node)
    

    def emOrdem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.emOrdem(node.esquerda)
        print(node, end=' ')
        if node.direita:
            self.emOrdem(node.direita)
    
    def preOrdem(self, node=None):
        if node is None:
            node = self.raiz
        print(node, end=' ')
        if node.esquerda:
            self.preOrdem(node.esquerda)
        if node.direita:
            self.preOrdem(node.direita)

    '''# Percurso em Nível 
 def levelorder_traversal(self, node=raiz):
        if node == raiz:
            node = self.raiz

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.esquerda:
                queue.push(node.esquerda)
            if node.direita:
                queue.push(node.direita)
            print(node, end=" ")'''


class BinarySearchTree(arvoreBinaria):
    
    def inserir(self, valor):
        parent = None
        x = self.raiz
        cont = 0
        while(x):
            parent = x
            if valor < x.dados:
                x = x.esquerda
            else:
                x = x.direita
            cont += 1
        if parent is None:
            self.raiz = Node(valor)
        elif valor < parent.dados:
            parent.esquerda = Node(valor)
        else:
            parent.direita = Node(valor)
        return cont 

    def busca(self, valor):
        return self._busca(valor, self.raiz)

    def _busca(self, valor, node):
        if node is None:
            return -1
        if node.dados == valor:
            return 0
        if valor < node.dados:
            aux = self._busca(valor, node.esquerda)
            return 1 + aux if aux >= 0 else aux
        aux = self._busca(valor, node.direita)
        return 1 + aux if aux >= 0 else aux

    # # Encontrando o MAIOR e o MENOR elemento numa ÁRVORE Binária de Busca
    def min(self, node=raiz):
        if node == raiz:
            node = self.raiz
        while node.esquerda:
            node = node.esquerda
        return node.dados

    def max(self, node=raiz):
        if node == raiz:
            node = self.raiz
        while node.direita:
            node = node.direita
        return node.dados

    # REMOVENDO da Árvore Binária de Busca
    def remove(self, valor, node=raiz):
        # Se for o valor padrão, executa a partir da raiz
        if node == raiz:
            node = self.raiz
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return -1
        # Se o valor for menor, desce à esquerda
        if valor < node.dados:
            node.esquerda = self.remove(valor, node.esquerda)
        # Se o valor for maior, desce à direita
        elif valor > node.dados:
            node.direita = self.remove(valor, node.direita)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.direita)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.dados = substitute
                # Depois, remove o substituto da subárvore à direita
                node.direita = self.remove(substitute, node.direita)

        return node

# tree =BinarySearchTree()         
# inicio = input()
# elemento = input().split()
# print(tree.altura())
# for x in elemento:
#     tree.inserir(x)
# comandos= input().split()
# while comandos[0] != "FIM":
#     if comandos[0] == "SCH":
#         resultadoBusca = tree.busca(comandos[1])
#         print(resultadoBusca)
#     elif comandos[0] == "INS":
#         print(tree.inserir(comandos[1]))
#     elif comandos[0]== "DEL":
#         pass
#     comandos= input().split()

a = "100 50 150 140 200 180 190 20 55 70 81"
tree = BinarySearchTree()

# # #     #tree.raiz.esquerda = Node(18)
# # #     #tree.raiz.direita = Node(14)
for i in a.split(" "):
    tree.inserir(int(i))

tree.preOrdem()
print()
print()
tree.emOrdem()
print()
print()
tree.posOrdem()
print()
print(tree.altura())
# tree.remove(150)
print(tree.busca(190))
tree.preOrdem()
print(tree.altura())


# #print(tree.raiz)
# #print(tree.raiz.direita)
# #print(tree.raiz.esquerda)
