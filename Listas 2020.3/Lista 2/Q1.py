class No:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0
    
    def __repr__(self):
        return int(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.depth = []

    def __len__(self):
        return self.size

    def insertAndPrint(self, key, value):
        cont = True
        no_current = self.root
        no_before = None
        depth = 1
        if type(key) == int and type(value) == str:
            while cont:
                if no_current is None:
                    print(1)
                    self.root = No(key, value)
                    self.size += 1
                    cont = False
                elif key < no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        print(depth)
                        self.depth.append(depth)
                        self.size += 1
                        cont = False
                elif key >= no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        print(depth)
                        self.depth.append(depth)
                        self.size += 1
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
                    self.size += 1
                    cont = False
                elif key < no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        self.depth.append((key, depth))
                        self.size += 1
                        cont = False
                elif key >= no_current.key:
                    depth += 1
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        self.depth.append((key, depth))
                        self.size += 1
                        cont = False
    

    def remover(self, key):
        self.root, value = self.__remover(self.root, key)
        return value
    
    def __remover(self, no, key):
        if no is None:
            raise KeyError(key)
        elif key > no.key:
            no.right, value = self.__remover(no.right, key)
        elif key < no.key:
            no.left, value = self.__remover(no.left, key)
        else:
            value = no.value
            if no.right is None:
                aux = no
                no = no.left
                del aux
            elif no.left is None:
                aux = no
                no = no.right
                del aux
            else:
                no.right = self.__sucessor(no, no.right)
        return no, value
    
    def __sucessor(self, no, nodo):
        '''
        Para promover um nó é necessário achar um entre os dois value possíveis
        para a substituição: o nó imediatamente anterior ao nó que vai ser
        substituído (antecessor) ou o imediatamente posterior (sucessor). Para
        essa implementação eu escolhi fazer a substituição pelo sucessor, mas
        a implementação com o antecessor pode ser vista nos slides do professor
        Renato.
        O antecessor é sempre o maior entre os menores (o mais a direita entre
        os nós a esquerda do nó que será substituído) e o sucessor é o menor
        entre os maiores (o mais a esquerda dos nós a direita).
        '''
        if nodo.left is not None:
            nodo.left = self.__sucessor(no, nodo.left)
        else:
            aux = nodo
            no.value = nodo.value
            no.key = nodo.key
            nodo = nodo.right
            del aux
        return nodo

    
    def remove___(self, key):
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
        return no_current.key

    def search(self, key):
        no = self.root
        depth = 1
        while no is not None:
            if (no.key == key) and no is self.root:
                return 1
            if no.key == key:
                return depth
            elif no.key < key:
                no = no.right
                depth += 1
            else:
                no = no.left
                depth += 1
        return -1





    def produndidade(self, no):
        if no == None or no.left == None and no.right == None:
            return 1
        else:
            if self.produndidade(no.left) > self.produndidade(no.right):
                return  1 + self.produndidade(no.left) 
            else:
                return  1 + self.produndidade(no.right) 


    def height(self, no):
        if no == None or no.left == None and no.right == None:
            return 1
        else:
            if self.height(no.left) > self.height(no.right):
                return  1 + self.height(no.left) 
            else:
                return  1 + self.height(no.right) 



 



inp = ["", "46 101 10 2 90 220 148 30 20 40 128 374 253 128 34 451 194 448 919 527 451"]

comands = ['INS 71', 'DEL 30', 'SCH 20']



aux = inp[1].split(" ")
arvore = BinarySearchTree()
for i in aux:
    # print(i + "->")
    arvore.insert(int(i), i[4::])




print(arvore.height(arvore.root))


print(arvore.search(101))
arvore.remover(101)

# print(arvore.height(arvore.root))


# print(arvore.height(arvore.root))

# print(arvore.search(100))
# for j in comands:
#     j = j.split(" ")
#     if j[0] == 'SCH':
#         print(arvore.search(int(j[1])))
#     elif j[0] == "INS":
#         arvore.insertAndPrint(int(j[1]), j[1])
#         # print((arvore.search(int(i[4::]))))
#     elif j[0] == "DEL":
#         print((arvore.search(int(j[1]))))
#         arvore.remove(int(j[1]))
print("######################################################")
print("######################################################")
print(arvore.height(arvore.root))



# arvore.remove(22)
# print(arvore.search(22))






# maior = 0
# for i in aux:
#     num = arvore.search(int(i))
#     if maior < num:
#         maior = num
# print(maior+1)


"""
def main():
    inputs = []
    cont = True
    try:
        while cont:
            inputs.append(input())
    except:
        pass
    
    num = inputs[0]
    aux = inputs[1].split(" ")
    lista = inputs[2::]

    arvore = BinarySearchTree()

    for i in aux:
        arvore.insert(int(i), i)

    print(arvore.deepSearch())

    for i in lista:
        if i[:3:] == "SCH":
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "INS":
            arvore.insertAndPrint(int(i[4::]), i)
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "DEL":
            print((arvore.search(int(i[4::]))))
            arvore.remove(int(i[4::]))
    
    print(arvore.deepSearch())

if __name__ == '__main__':
    main()
"""