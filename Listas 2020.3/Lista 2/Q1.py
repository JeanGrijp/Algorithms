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
        '''
        3 casos:

        Caso 1
        o nó a ser removido não tem filhos
        esse caso é simples, basta setar a ligação
        do pai para None

        Caso 2
        o nó a ser removido tem somente 1 filho
        basta colocar o seu filho no lugar dele

        Caso 3
        o nó a ser removido possui dois filhos
        basta pegar o menor elemento da subárvore à right
		'''
        key = int(key)
        no_current = self.root
        no_before = None
        while no_current is not None:
            # verifica se encontrou o nó a ser removido
            if no_current.key == key:






                # caso 1: o nó a ser removido não possui filhos (nó folha)
                if no_current.left is None and no_current.right is None:
                    # verifica se é a root
                    if no_before is None:
                        # print(-1)
                        self.root = None
                        self.size = 0
                    else:
                        # verifica se é filho à left ou à right
                        if no_before.left == no_current:
                            # print(self.search(no_current)[1])
                            no_before.left = None
                            self.size -= 1

                        elif no_before.right == no_current:
                            # print(self.search(no_current)[1])
                            no_before.right = None
                            self.size -= 1






                # caso 2: o nó a ser removido possui somente um filho
                elif (no_current.left is None and no_current.right is not None) or (no_current.left is not None and no_current.right is None):
                    # verifica se o nó a ser removido é a root
                    if no_before is None:
                        # verifica se o filho de no_current é filho à left
                        if no_current.left is not None:
                            # print(self.search(no_current)[1])
                            self.root = no_current.left
                            self.size -= 1
                        else:
                             # senão o filho de no_current é filho à right
                            # print(self.search(no_current)[1])
                            self.root = no_current.right
                            self.size -= 1
                    else:
                        # verifica se o filho de no_current é filho à left
                        if no_current.left is not None:
                            # verifica se no_current é filho à left de no_before
                            if no_before.left == no_current:
                                # print(self.search(no_current)[1])
                                no_before.left = no_current.left
                            else:# senão no_current é filho à right
                                # print(self.search(no_current)[1])
                                no_before.right = no_current.left
                        else:# senão o filho de no_current é filho à right
                            # verifica se no_current é filho à left
                            if no_before.left == no_current:
                                # print(self.search(no_current)[1])
                                no_before.left = no_current.right
                            else:# senão no_current é filho à right
                                # print(self.search(no_current)[1])
                                no_before.right = no_current.right






                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da subárvore à direita
                elif (no_current.left is not None) and (no_current.right is not None):
                    
                    menor_no_before = no_current
                    menor_no = no_current.right
                    proximo_menor = no_current.right.left
                    
                    while proximo_menor is not None:
                        menor_no_before = menor_no
                        menor_no = proximo_menor
                        proximo_menor = menor_no.left
                    # verifica se o nó a ser removido é a root
                    if no_before is None:
                        # Caso especial: o nó que vai ser a nova root é filho da root
                        if self.root.right.key == menor_no.key:
                            # print(self.search(no_current)[1])
                            menor_no.left = self.root.left
                        else:
                            '''
								verifica se o menor_no é filho à left ou à right
								para setar para None o menor_no
							'''
                            if menor_no_before.left.key == menor_no.key:
                                # print(self.search(no_current)[1])
                                menor_no_before.left = None
                            else:
                                # print(self.search(no_current)[1])
                                menor_no_before.right = None
                            # seta os filhos à right e left de menor_no
                            menor_no.left = no_current.left
                            menor_no.right = no_current.right
                        # faz com que o menor_no seja a root
                        self.root = menor_no
                    else:
                        '''
							verifica se no_current é filho à left ou à right
							para setar o menor_no como filho do pai do no_current (no_before)
						'''
                        if no_before.left.key == no_current.key:
                            # print(self.search(no_current)[1])
                            no_before.left = menor_no
                        else:
                            # print(self.search(no_current)[1])
                            no_before.right = menor_no
                        '''
							verifica se o menor_no é filho à left ou à right
							para setar para None o menor_no
						'''
                        if menor_no_before.left.key == menor_no.key:
                            # print(self.search(no_current)[1])
                            menor_no_before.left = None
                        else:
                            # print(self.search(no_current)[1])
                            menor_no_before.right = None

						# seta os filhos à right e left de menor_no
                        menor_no.left = no_current.left
                        menor_no.right = no_current.right
                break 
            no_before = no_current

            # verifica se vai para left ou right
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
