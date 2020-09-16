import sys
sys.setrecursionlimit(sys.getrecursionlimit())
class No:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return int(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return self.size

    def insertAndPrint(self, key, value):
        cont = True
        noAtual = self.root
        noSentinela = None
        depth = 0
        if type(key) == int and type(value) == str:
            while cont:
                if noAtual is None:
                    print(0)
                    self.root = No(key, value)
                    cont = False
                elif key < noAtual.key:
                    depth += 1
                    noSentinela = noAtual
                    noAtual = noAtual.left
                    if noAtual is None:
                        noSentinela.left = No(key, value)
                        print(depth)
                        cont = False
                elif key >= noAtual.key:
                    depth += 1
                    noSentinela = noAtual
                    noAtual = noAtual.right
                    if noAtual is None: 
                        noSentinela.right = No(key, value)
                        print(depth)
                        cont = False

    def insert(self, key, value):
        cont = True
        noAtual = self.root
        noSentinela = None
        if type(key) == int and type(value) == str:
            while cont:
                if noAtual is None:
                    self.root = No(key, value)
                    cont = False
                elif key < noAtual.key:
                    noSentinela = noAtual
                    noAtual = noAtual.left
                    if noAtual is None:
                        noSentinela.left = No(key, value)
                        cont = False
                elif key >= noAtual.key:
                    noSentinela = noAtual
                    noAtual = noAtual.right
                    if noAtual is None: 
                        noSentinela.right = No(key, value)
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
    



    def remove(self, key):
        if self.root is None:
            return
        no = self.root
        noAtual = self.root
        noSentinela = None
        while noAtual is not None:
            if noAtual.key < key:
                noSentinela = noAtual
                noAtual = noAtual.right
            elif noAtual.key > key:
                noSentinela = noAtual
                noAtual = noAtual.left
            elif noAtual.key == key:
                if (noAtual.left is None) and (noAtual.right is None):
                    if noSentinela is None:
                        self.root = None
                    elif noSentinela.left.key == noAtual.key:
                        noSentinela.left = None
                    elif noSentinela.right == noAtual.key:
                        noSentinela.right = None
                elif (noAtual.left is None and noAtual.right is not None) or (noAtual.left is not None and noAtual.right is None):
                    if noSentinela is None:
                        if noAtual.left is not None:
                            self.root = noAtual.left
                        else:
                            self.root = noAtual.right
                    else:
                        if noAtual.left is not None:
                            if noSentinela.left == noAtual:
                                noSentinela.left = noAtual.left
                            else:
                                noSentinela.right = noAtual.left
                        else:
                            if noSentinela.left == noAtual:
                                noSentinela.left = noAtual.right
                            else:
                                noSentinela.right = noAtual.right
                

                elif (noAtual.left is not None) and (noAtual.right is not None):
                    terceiro = noAtual
                    segundo = noAtual.right
                    primeiro = noAtual.right.left               
                    while primeiro is not None:
                        terceiro = segundo
                        segundo = primeiro
                        primeiro = segundo.left
                    if noSentinela is None:
                        if self.root.right.key == segundo.key:
                            segundo.left = self.root.left
                        else:
                            if terceiro.left.key == segundo.key:
                                terceiro.left = None
                            else:
                                terceiro.right = None
                            segundo.left = noAtual.left
                            segundo.right = noAtual.right
                        self.root = segundo
                    else:
                        if noSentinela.left.key == noAtual.key:
                            noSentinela.left = segundo
                        else:
                            noSentinela.right = segundo
                        if terceiro.left.key == segundo.key:
                            terceiro.left = None
                        else:
                            terceiro.right = None
                        segundo.left = noAtual.left
                        segundo.right = noAtual.right
                break 


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


    def height(self, no):
        if no == None or no.left == None and no.right == None:
            return 1
        else:
            if self.height(no.left) > self.height(no.right):
                return  1 + self.height(no.left) 
            else:
                return  1 + self.height(no.right) 

    def pre_ordem(self, no):
        if no is None:
            return
        a = "{}:'{}'".format(no.key, no.value)
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
        a = "{}:'{}'".format(no.key, no.value)
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
        a = "{}:'{}'".format(no.key, no.value)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string


tree = BinarySearchTree()
a = "100 50 150 140 200 180 190 20 55 70 81"
for i in a.split(" "):
    print(i+"->")
    tree.insertAndPrint(int(i), i)


print(tree.pre_ordem(tree.root))

tree.remove(150)
# tree.pre_ordem(tree.root)
# print(tree.search(190))
print(tree.pre_ordem(tree.root))

# def main():
#     arvore = BinarySearchTree()
#     inp = int(input())
#     for i in input().split(" "):
#         arvore.insert(int(i), i)
#     print(arvore.height(arvore.root))
#     cont = True
#     while cont:
#         inp = input()
#         if inp[:3:] == 'SCH':
#             print(arvore.search(int(inp[4::])))
#         elif inp[:3:] == "INS":
#             arvore.insertAndPrint(int(inp[4::]), inp[4::])
#         elif inp[:3:] == "DEL":
#             print((arvore.search(int(inp[4::]))))
#             arvore.remove(int(inp[4::]))
#         elif inp == "END":
#             print(arvore.height(arvore.root))
#             break

# if __name__ == '__main__':
#     main()