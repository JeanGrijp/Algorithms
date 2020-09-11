inp = [100, "460 10 0 120 90 30 20 40 70 50 60 80 100 110 140 130 190 180 170 150 160 220 210 200 380 270 260 230 250 240 310 280 300 290 350 330 320 340 360 370 440 390 400 420 410 430 450 580 550 500 470 480 490 540 520 510 530 570 560 980 850 780 720 700 600 590 670 620 610 650 640 630 660 680 690 710 730 740 770 750 760 810 790 800 820 830 840 970 860 920 890 870 880 900 910 950 930 940 960 990"]

comands = ['INS 128', 'INS 374', 'INS 253', 'INS 128', 'INS 34', 'INS 451', 'INS 194', 'INS 448', 'INS 919', 'INS 527', 'INS 62', 'INS 541', 'INS 183', 'INS 458', 'INS 654', 'INS 321', 'INS 597', 'INS 5', 'INS 539', 'INS 641', 'INS 643', 'INS 167', 'INS 769', 'INS 689', 'INS 60', 'INS 280', 'INS 146', 'INS 706', 'INS 247', 'INS 981', 'INS 721', 'INS 243', 'INS 980', 'INS 33', 'INS 852', 'INS 887', 'INS 433', 'INS 904', 'INS 888', 'INS 587', 'INS 641', 'INS 180', 'INS 36', 'INS 333', 'INS 740', 'INS 417', 'INS 745', 'INS 755', 'INS 533', 'INS 308', 'INS 739', 'INS 423', 'INS 423', 'INS 44', 'INS 895', 'INS 208', 'INS 770', 'INS 819', 'INS 737', 'INS 743', 'INS 705', 'INS 631', 'INS 955', 'INS 822', 'INS 587', 'INS 717', 'INS 82', 'INS 299', 'INS 919', 'INS 635', 'INS 712', 'INS 737', 'INS 291', 'INS 404', 'INS 743', 'INS 287', 'INS 86', 'INS 275', 'INS 790', 'INS 737', 'INS 548', 'INS 663', 'INS 840', 'INS 560', 'INS 277', 'INS 650', 'INS 6', 'INS 136', 'INS 940', 'INS 431', 'INS 960', 'INS 343', 'INS 773', 'INS 308', 'INS 208', 'INS 914', 'INS 747', 'INS 481', 'INS 378', 'INS 976', 'END']


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