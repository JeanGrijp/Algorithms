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
        depth = 0
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
        # return no_current.key

    def search(self, key):
        no = self.root
        depth = 0
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

 



inp = ["", "640 550 220 210 170 130 110 60 40 20 10 0 30 50 100 90 70 80 120 160 140 150 200 190 180 230 480 290 240 280 270 260 250 440 390 380 340 330 310 300 320 350 360 370 420 410 400 430 450 470 460 490 510 500 540 530 520 630 600 560 590 580 570 610 620 700 680 650 670 660 690 840 710 830 750 740 730 720 820 770 760 790 780 810 800 850 900 890 880 860 870 940 930 910 920 960 950 970 980 990"]

# inp = ["", "100 50 150 140 200 180 190"]


comands = ['INS 128', 'INS 374', 'INS 253', 'INS 128', 'INS 34', 'INS 451', 'INS 194', 'INS 448', 'INS 919', 'INS 527', 'INS 62', 'INS 541', 'INS 183', 'INS 458', 'INS 654', 'INS 321', 'INS 597', 'INS 5', 'INS 539', 'INS 641', 'INS 643', 'INS 167', 'INS 769', 'INS 689', 'INS 60', 'INS 280', 'INS 146', 'INS 706', 'INS 247', 'INS 981', 'INS 721', 'INS 243', 'INS 980', 'INS 33', 'INS 852', 'INS 887', 'INS 433', 'INS 904', 'INS 888', 'INS 587', 'INS 641', 'INS 180', 'INS 36', 'INS 333', 'INS 740', 'INS 417', 'INS 745', 'INS 755', 'INS 533', 'INS 308', 'INS 739', 'INS 423', 'INS 423', 'INS 44', 'INS 895', 'INS 208', 'INS 770', 'INS 819', 'INS 737', 'INS 743', 'INS 705', 'INS 631', 'INS 955', 'INS 822', 'INS 587', 'INS 717', 'INS 82', 'INS 299', 'INS 919', 'INS 635', 'INS 712', 'INS 737', 'INS 291', 'INS 404', 'INS 743', 'INS 287', 'INS 86', 'INS 275', 'INS 790', 'INS 737', 'INS 548', 'INS 663', 'INS 840', 'INS 560', 'INS 277', 'INS 650', 'INS 6', 'INS 136', 'INS 940', 'INS 431', 'INS 960', 'INS 343', 'INS 773', 'INS 308', 'INS 208', 'INS 914', 'INS 747', 'INS 481', 'INS 378', 'INS 976']


aux = inp[1].split(" ")
arvore = BinarySearchTree()
for i in aux:
    print(i + "->")
    arvore.insertAndPrint(int(i), i[4::])


print("Altura inicial -> "+ str(arvore.height(arvore.root)))

# print(arvore.height(arvore.root))

print("####### Pré Ordem ########")
print(arvore.pre_ordem(arvore.root))
print("##########################")


print("$$$$$$$$ Comands $$$$$$$$$$")
for j in comands:
    j = j.split(" ")
    if j[0] == 'SCH':
        print(arvore.search(int(j[1])))
    elif j[0] == "INS":
        arvore.insertAndPrint(int(j[1]), j[1])
    elif j[0] == "DEL":
        print((arvore.search(int(j[1]))))
        arvore.remover(int(j[1]))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("####### Pré Ordem ########")
print(arvore.pre_ordem(arvore.root))
print("##########################")


print("Altura final -> "+ str(arvore.height(arvore.root)))



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

    print(arvore.height(arvore.root))

    for i in lista:
        if i[:3:] == "SCH":
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "INS":
            arvore.insertAndPrint(int(i[4::]), i)
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "DEL":
            print((arvore.search(int(i[4::]))))
            arvore.remove(int(i[4::]))
    
    print(arvore.height(arvore.root))

if __name__ == '__main__':
    main()
"""