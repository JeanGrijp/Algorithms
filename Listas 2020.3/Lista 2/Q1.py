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
        no_current = self.root
        no_before = None
        depth = 0
        if type(key) == int and type(value) == str:
            while cont:
                if no_current is None:
                    print(1)
                    self.root = No(key, value)
                    cont = False
                elif key < no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        print(depth)
                        cont = False
                elif key >= no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        print(depth)
                        cont = False

    def insert(self, key, value):
        cont = True
        no_current = self.root
        no_before = None
        depth = 1
        if type(key) == int and type(value) == str:
            while cont:
                if no_current is None:
                    self.root = No(key, value)
                    cont = False
                elif key < no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        cont = False
                elif key >= no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
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


    def remove(self, key):
        key = int(key)
        no_current = self.root
        no_before = None
        while no_current is not None:
            if no_current.key == key:
                if no_current.left is None and no_current.right is None:
                    if no_before is None:
                        self.root = None
                        self.size = 0
                    else:
                        if no_before.left == no_current:
                            no_before.left = None
                            self.size -= 1
                        elif no_before.right == no_current:
                            no_before.right = None
                            self.size -= 1
                elif (no_current.left is None and no_current.right is not None) or (no_current.left is not None and no_current.right is None):
                    if no_before is None:
                        if no_current.left is not None:
                            self.root = no_current.left
                            self.size -= 1
                        else:
                            self.root = no_current.right
                            self.size -= 1
                    else:
                        if no_current.left is not None:
                            if no_before.left == no_current:
                                no_before.left = no_current.left
                            else:
                                no_before.right = no_current.left
                        else:
                            if no_before.left == no_current:
                                no_before.left = no_current.right
                            else:
                                no_before.right = no_current.right
                elif (no_current.left is not None) and (no_current.right is not None):
                    menor_no_before = no_current
                    menor_no = no_current.right
                    proximo_menor = no_current.right.left               
                    while proximo_menor is not None:
                        menor_no_before = menor_no
                        menor_no = proximo_menor
                        proximo_menor = menor_no.left
                    if no_before is None:
                        if self.root.right.key == menor_no.key:
                            menor_no.left = self.root.left
                        else:
                            if menor_no_before.left.key == menor_no.key:
                                menor_no_before.left = None
                            else:
                                menor_no_before.right = None
                            menor_no.left = no_current.left
                            menor_no.right = no_current.right
                        self.root = menor_no
                    else:
                        if no_before.left.key == no_current.key:
                            no_before.left = menor_no
                        else:
                            no_before.right = menor_no
                        if menor_no_before.left.key == menor_no.key:
                            menor_no_before.left = None
                        else:
                            menor_no_before.right = None
                        menor_no.left = no_current.left
                        menor_no.right = no_current.right
                break 
            no_before = no_current
            if key < no_current.key:
                no_current = no_current.left
            else:
                no_current = no_current.right


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


def main():
    arvore = BinarySearchTree()
    inp = int(input())
    for i in input().split(" "):
        arvore.insert(int(i), i)
    print(arvore.height(arvore.root))
    cont = True
    while cont:
        inp = input()
        if inp[:3:] == 'SCH':
            print(arvore.search(int(inp[4::])))
        elif inp[:3:] == "INS":
            arvore.insertAndPrint(int(inp[4::]), inp[4::])
        elif inp[:3:] == "DEL":
            print((arvore.search(int(inp[4::]))))
            arvore.remover(int(inp[4::]))
        elif inp == "END":
            print(arvore.height(arvore.root))
            break

if __name__ == '__main__':
    main()