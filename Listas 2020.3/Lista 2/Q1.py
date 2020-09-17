# import sys
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

    def sucessor(self, no):
        paidosucessor = no
        sucessor = no
        atual = no.right
        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.left
        if sucessor != no.right:
            paidosucessor.left = sucessor.right
            sucessor.right = no.right
        return sucessor

    def remover(self, key):
        if self.root == None:
            return
        atual = self.root
        pai = self.root
        filho_left = True
        while atual.key != key:
            pai = atual
            if key < atual.key:
                atual = atual.left
                filho_left = True
            else:
                atual = atual.right 
                filho_left = False
            if atual == None:
                return
        if atual.left == None and atual.right == None:
            if atual == self.root:
                self.root = None
            else:
                if filho_left:
                        pai.left.left =  None 
                else:
                        pai.right = None
        elif atual.right == None:
            if atual == self.root:
                self.root = atual.left
            else:
                if filho_left:
                        pai.left = atual.left
                else:
                        pai.right = atual.left
        elif atual.left == None:
            if atual == self.root:
                self.root = atual.right
            else:
                if filho_left:
                        pai.left = atual.right
                else:
                        pai.right = atual.right
        else:
            sucessor = self.sucessor(atual)
            if atual == self.root:
                self.root = sucessor
            else:
                if filho_left:
                        pai.left = sucessor
                else:
                        pai.right = sucessor
            sucessor.left = atual.left





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


tree = BinarySearchTree()
a = "100 50 150 140 200 180 190 20 55 70 81"
for i in a.split(" "):
    print(i+"->")
    tree.insertAndPrint(int(i))


print(tree.pre_ordem(tree.root))

print(tree.search(190))

tree.remover(150)
print(tree.search(190))
# tree.pre_ordem(tree.root)
# print(tree.search(190))
print(tree.pre_ordem(tree.root))

# def main():
#     arkeyore = BinarySearchTree()
#     inp = int(input())
#     for i in input().split(" "):
#         arkeyore.insert(int(i), i)
#     print(arkeyore.height(arkeyore.root))
#     cont = True
#     while cont:
#         inp = input()
#         if inp[:3:] == 'SCH':
#             print(arkeyore.search(int(inp[4::])))
#         elif inp[:3:] == "INS":
#             arkeyore.insertAndPrint(int(inp[4::]), inp[4::])
#         elif inp[:3:] == "DEL":
#             print((arkeyore.search(int(inp[4::]))))
#             arkeyore.remokeye(int(inp[4::]))
#         elif inp == "END":
#             print(arkeyore.height(arkeyore.root))
#             break

# if __name__ == '__main__':
#     main()