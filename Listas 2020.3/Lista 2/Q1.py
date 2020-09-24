import random
import time
import sys

# sys.setrecursionlimit(sys.getrecursionlimit())


class No:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
    def __repr__(self):
        return int(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return self.size

    def insertAndPrint(self, key):
        cont = True
        noAtual = self.root
        noSentinela = None
        depth = 0
        if type(key) == int:
            while cont:
                if noAtual is None:
                    print(0)
                    self.root = No(key)
                    cont = False
                elif key < noAtual.key:
                    depth += 1
                    noSentinela = noAtual
                    noAtual = noAtual.left
                    if noAtual is None:
                        noSentinela.left = No(key)
                        print(depth)
                        cont = False
                elif key >= noAtual.key:
                    depth += 1
                    noSentinela = noAtual
                    noAtual = noAtual.right
                    if noAtual is None: 
                        noSentinela.right = No(key)
                        print(depth)
                        cont = False

    def insert(self, key):
        cont = True
        noAtual = self.root
        noSentinela = None
        if type(key) == int:
            while cont:
                if noAtual is None:
                    self.root = No(key)
                    cont = False
                elif key < noAtual.key:
                    noSentinela = noAtual
                    noAtual = noAtual.left
                    if noAtual is None:
                        noSentinela.left = No(key)
                        cont = False
                elif key >= noAtual.key:
                    noSentinela = noAtual
                    noAtual = noAtual.right
                    if noAtual is None: 
                        noSentinela.right = No(key)
                        cont = False

    def remover(self, key):
        self.root = self.removerRec(self.root, key)

    def removerRec(self, no, key):
        if no is None:
            pass
        elif key > no.key:
            no.right = self.removerRec(no.right, key)
        elif key < no.key:
            no.left = self.removerRec(no.left, key)
        else:
            if no.right is None:
                aux = no
                no = no.left
                del aux
            elif no.left is None:
                aux = no
                no = no.right
                del aux
            else:
                no.right = self.sucessor(no, no.right)
        return no
    
    def sucessor(self, no, nodo):
        if nodo.left is not None:
            nodo.left = self.sucessor(no, nodo.left)
        else:
            aux = nodo
            no.value = nodo.value
            no.key = nodo.key
            nodo = nodo.right
            del aux
        return nodo


    # def sucessor(self, no):
    #     if 
    #     paiDoSucessor = no
    #     sucessor = no
    #     atual = no.right
    #     while atual != None:
    #         paiDoSucessor = sucessor
    #         sucessor = atual
    #         atual = atual.left
    #     if sucessor != no.right:
    #         paiDoSucessor.left = sucessor.right
    #         sucessor.right = no.right
    #     return sucessor

    # def remover(self, key):
    #     if self.root == None:
    #         return
    #     atual = self.root
    #     pai = self.root
    #     filho_left = True
    #     while atual.key != key:
    #         pai = atual
    #         if key < atual.key:
    #             atual = atual.left
    #             filho_left = True
    #         else:
    #             atual = atual.right 
    #             filho_left = False
    #         if atual == None:
    #             return
    #     if atual.left == None and atual.right == None:
    #         if atual == self.root:
    #             self.root = None
    #         else:
    #             if filho_left:
    #                     pai.left.left =  None 
    #             else:
    #                     pai.right = None
    #     elif atual.right == None:
    #         if atual == self.root:
    #             self.root = atual.left
    #         else:
    #             if filho_left:
    #                     pai.left = atual.left
    #             else:
    #                     pai.right = atual.left
    #     elif atual.left == None:
    #         if atual == self.root:
    #             self.root = atual.right
    #         else:
    #             if filho_left:
    #                     pai.left = atual.right
    #             else:
    #                     pai.right = atual.right
    #     else:
    #         sucessor = self.sucessor(atual)
    #         if atual == self.root:
    #             self.root = sucessor
    #         else:
    #             if filho_left:
    #                     pai.left = sucessor
    #             else:
    #                     pai.right = sucessor
    #         sucessor.left = atual.left

    def search(self, key):
        no = self.root
        depth = 0
        if self.root is None:
            return 0
        if (no.key == key) and no is self.root:
            return 1
        while no is not None:
            if no.key == key:
                return depth
            elif no.key < key:
                no = no.right
                depth += 1
            else:
                no = no.left
                depth += 1
        return -1

    def maximo(self, a, b):
        if a > b:
            return a
        return b

    def height(self, no):
        if no is None:
            return 0
        return 1 + self.maximo(self.height(no.left), self.height(no.right))

    def pre_ordem(self, no):
        if no is None:
            return
        a = "{}:'{}'".format(no.key, no.key)
        b = self.pre_ordem(no.left)
        c = self.pre_ordem(no.right)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string

    def ordem(self, no):
        if no is None:
            return
        b = self.ordem(no.left)
        a = "{}:'{}'".format(no.key, no.key)
        c = self.ordem(no.right)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string


    def pos_ordem(self, no):
        if no is None:
            return
        b = self.ordem(no.left)
        c = self.ordem(no.right)
        a = "{}:'{}'".format(no.key, no.key)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string



inp = ""
for i in range(10000):
    inp += str(random.randint(0, 10000))

# print(inp)
lista = ['INS', 'DEL', 'SCH']
aux = []
cont = 0
while cont < 10000:
    aux.append("{} {}".format(lista[random.randint(0, 2)], random.randint(0, 10000)))
    cont += 1
print(aux)

tempo1 = time.time_ns()
arvore = BinarySearchTree()

for i in inp.split(" "):
    arvore.insert(int(i))
print(arvore.height(arvore.root))
cont = True
for j in aux:
    if j[:3:] == 'SCH':
        print(arvore.search(int(j[4::])))
    elif j[:3:] == "INS":
        arvore.insertAndPrint(int(j[4::]))
    elif j[:3:] == "DEL":
        print((arvore.search(int(j[4::]))))
        arvore.remover(int(j[4::]))


print(arvore.height(arvore.root))



tempo2 = time.time_ns()
tempo = (tempo2 - tempo1) / 1000000
print("Tempo: %i ms"%tempo)




# def main():
#     arvore = BinarySearchTree()
#     inp = int(input())
#     for i in input().split(" "):
#         arvore.insert(int(i))
#     print(arvore.height(arvore.root))
#     cont = True
#     while cont:
#         inp = input()
#         if inp[:3:] == 'SCH':
#             print(arvore.search(int(inp[4::])))
#         elif inp[:3:] == "INS":
#             arvore.insertAndPrint(int(inp[4::]))
#         elif inp[:3:] == "DEL":
#             print((arvore.search(int(inp[4::]))))
#             arvore.remover(int(inp[4::]))
#         elif inp == "END":
#             print(arvore.height(arvore.root))
#             break

# if __name__ == '__main__':
#     main()