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
                    print(self.search(key)[1])
                    self.size += 1
                    cont = False
                elif key < no_current.key:
                    no_before = no_current
                    no_current = no_current.left
                    if no_current is None:
                        no_before.left = No(key, value)
                        print(self.search(key)[1])
                        self.size += 1
                        cont = False
                elif key >= no_current.key:
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        print(self.search(no_current)[1])
                        self.size += 1
                        cont = False

    def search(self, key):
        no = self.root
        depth = 0
        while no is not None:
            if no.key == key:
                return no.key, depth
            elif no.key > key:
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
                        print(-1)
                        self.root = None
                        self.size = 0
                    else:
                        # verifica se é filho à left ou à right
                        if no_before.left == no_current:
                            print(self.search(no_current)[1])
                            no_before.left = None
                            self.size -= 1

                        elif no_before.right == no_current:
                            print(self.search(no_current)[1])
                            no_before.right = None
                            self.size -= 1






                # caso 2: o nó a ser removido possui somente um filho
                elif (no_current.left is None and no_current.right is not None) or (no_current.left is not None and no_current.right is None):
                    # verifica se o nó a ser removido é a root
                    if no_before is None:
                        # verifica se o filho de no_current é filho à left
                        if no_current.left is not None:
                            print(self.search(no_current)[1])
                            self.root = no_current.left
                            self.size -= 1
                        else:
                             # senão o filho de no_current é filho à right
                            print(self.search(no_current)[1])
                            self.root = no_current.right
                            self.size -= 1
                    else:
                        # verifica se o filho de no_current é filho à left
                        if no_current.left is not None:
                            # verifica se no_current é filho à left de no_before
                            if no_before.left == no_current:
                                print(self.search(no_current)[1])
                                no_before.left = no_current.left
                            else:# senão no_current é filho à right
                                print(self.search(no_current)[1])
                                no_before.right = no_current.left
                        else:# senão o filho de no_current é filho à right
                            # verifica se no_current é filho à left
                            if no_before.left == no_current:
                                print(self.search(no_current)[1])
                                no_before.left = no_current.right
                            else:# senão no_current é filho à right
                                print(self.search(no_current)[1])
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
                            print(self.search(no_current)[1])
                            menor_no.left = self.root.left
                        else:
                            '''
								verifica se o menor_no é filho à left ou à right
								para setar para None o menor_no
							'''
                            if menor_no_before.left.key == menor_no.key:
                                print(self.search(no_current)[1])
                                menor_no_before.left = None
                            else:
                                print(self.search(no_current)[1])
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
                            print(self.search(no_current)[1])
                            no_before.left = menor_no
                        else:
                            print(self.search(no_current)[1])
                            no_before.right = menor_no
                        '''
							verifica se o menor_no é filho à left ou à right
							para setar para None o menor_no
						'''
                        if menor_no_before.left.key == menor_no.key:
                            print(self.search(no_current)[1])
                            menor_no_before.left = None
                        else:
                            print(self.search(no_current)[1])
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



inp = ['100', '570 250 0 220 60 40 10 20 30 50 200 80 70 170 150 140 110 100 90 120 130 160 190 180 210 230 240 280 260 270 310 300 290 450 380 360 350 320 330 340 370 390 420 400 410 440 430 470 460 520 490 480 500 510 550 530 540 560 940 760 630 590 580 610 600 620 650 640 700 690 670 660 680 720 710 730 740 750 860 840 770 780 790 830 800 820 810 850 870 890 880 930 900 910 920 980 970 950 960 990', 'SCH 1008', 'SCH 280', 'SCH 100', 'SCH 1006', 'SCH 200', 'SCH 490', 'SCH 210', 'SCH 480', 'SCH 700', 'SCH 930', 'SCH 940', 'SCH 1001', 'SCH 1002', 'SCH 1005', 'SCH 790', 'SCH 1004', 'SCH 990', 'SCH 820', 'SCH 1008', 'SCH 880', 'SCH 120', 'SCH 1003', 'SCH 1000', 'SCH 880', 'SCH 70', 'SCH 200', 'SCH 220', 'SCH 340', 'SCH 800', 'SCH 170', 'SCH 120', 'SCH 620', 'SCH 1005', 'SCH 750', 'SCH 1008', 'SCH 390', 'SCH 1001', 'SCH 220', 'SCH 1006', 'SCH 560', 'SCH 350', 'SCH 1005', 'SCH 1000', 'SCH 830', 'SCH 800', 'SCH 1001', 'SCH 1000', 'SCH 1002', 'SCH 1007', 'SCH 210', 'SCH 270', 'SCH 1004', 'SCH 410', 'SCH 1001', 'SCH 1004', 'SCH 500', 'SCH 1005', 'SCH 540', 'SCH 300', 'SCH 150', 'SCH 1003', 'SCH 1009', 'SCH 1002', 'SCH 530', 'SCH 1006', 'SCH 170', 'SCH 840', 'SCH 1008', 'SCH 1007', 'SCH 680', 'SCH 1003', 'SCH 1009', 'SCH 860', 'SCH 20', 'SCH 470', 'SCH 1004', 'SCH 600', 'SCH 1000', 'SCH 530', 'SCH 1003', 'SCH 1000', 'SCH 1005', 'SCH 1005', 'SCH 930', 'SCH 1007', 'SCH 390', 'SCH 460', 'SCH 610', 'SCH 1000', 'SCH 1006', 'SCH 1007', 'SCH 1003', 'SCH 410', 'SCH 390', 'SCH 1008', 'SCH 870', 'SCH 1001', 'SCH 1007', 'SCH 1001', 'SCH 1006', 'END']
aux = inp[1].split(" ")


arvore = BinarySearchTree()
arvore.insert(8, "8")
arvore.insert(7, "7")
arvore.insert(16, "16")
arvore.insert(5, "5")
arvore.insert(9, "9")
arvore.insert(17, "17")
arvore.insert(90, "90")
arvore.insert(900, "900")
print()
print(arvore.search(900))
print()
arvore.remove(5)


