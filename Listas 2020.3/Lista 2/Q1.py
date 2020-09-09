class No:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size


    def insert(self, key, value):
        cont = True
        no_current = self.root
        no_before = None
        if type(key) == int and type(value) == str:
            while cont:
                if no_current is None:
                    self.root = No(key, value)
                    self.size += 1
                    cont = False
                elif key < no_current.key:
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        self.size += 1
                        cont = False
                elif key >= no_current.key:
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        self.size += 1
                        cont = False

    def search(self, key):
        no = self.root
        depth = 0
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
        return no_current.value


'''
inp = "460 10 0 120 90 30 20 40 70 50 60 80 100 110 140 130 190 180 170 150 160 220 210 200 380 270 260 230 250 240 310 280 300 290 350 330 320 340 360 370 440 390 400 420 410 430 450 580 550 500 470 480 490 540 520 510 530 570 560 980 850 780 720 700 600 590 670 620 610 650 640 630 660 680 690 710 730 740 770 750 760 810 790 800 820 830 840 970 860 920 890 870 880 900 910 950 930 940 960 990"




aux = inp[0].split(" ")

num = inp[0]
lista = inp[2::]

arvore = BinarySearchTree()

for i in aux:
    arvore.insert(int(i), i)


maior = 0
for i in aux:
    num = arvore.search(int(i))
    if maior < num:
        maior = num
print(maior)

for i in lista:
    if i[:3:] == "SCH":
        print((arvore.search(int(i[4::]))))
    elif i[:3:] == "INS":
        arvore.insert(int(i[4::]), i)
        print((arvore.search(int(i[4::]))))
    elif i[:3:] == "DEL":
        arvore.remove(int(i[4::]))
        print((arvore.search(int(i[4::]))))
'''

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


    maior = 0
    for i in aux:
        num = arvore.search(int(i))
        if maior < num:
            maior = num
    print(maior)

    for i in lista:
        if i[:3:] == "SCH":
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "INS":
            arvore.insert(int(i[4::]), i)
            print((arvore.search(int(i[4::]))))
        elif i[:3:] == "DEL":
            print((arvore.search(int(i[4::]))))
            arvore.remove(int(i[4::]))
    
    maior = 0
    for i in aux:
        num = arvore.search(int(i))
        if maior < num:
            maior = num
    print(maior)

if __name__ == '__main__':
    main()
