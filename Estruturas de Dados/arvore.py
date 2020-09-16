class No:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        cont = True
        noAtual = self.root
        noSentinela = None
        if type(key) == int and type(value) == str:
            while cont:
                if noAtual is None:
                    # arvore ta vazia
                    self.root = No(key, value)
                    self.size += 1
                    cont = False
                elif key < noAtual.key:
                    noSentinela = noAtual  #só pra guardar a referência do No before
                    noAtual = noAtual.left# o No atual avança pra left do no before
                    if noAtual is None:# se True, é porque o value que eu quero insert é menor que o ultimo nó da arvore(folha)
                        noSentinela.left = No(key, value) #a importância de guardar a referencia before.
                        self.size += 1
                        cont = False
                elif key > noAtual.key:# aqui o value que eu quero insert é maior que o no current
                    noSentinela = noAtual
                    noAtual = noAtual.right
                    if noAtual is None: #se True, o value que é maior que a folha da arvore.
                        noSentinela.right = No(key, value)
                        self.size += 1
                        cont = False
                elif key == noAtual.key: # aqui é pra caso for igual, apenas substituir, outra opção era não fazer nada.
                    noAtual = No(key, value)
                    self.size += 1
                    cont = False


    def search(self, key):
        no = self.root
        while no is not None:
            if no.key == key:
                return no.value
            elif key > no.key:
                no = no.right
            else:
                no = no.left
        raise KeyError(key)


    def __len__(self):
        return self.size


    def remove(self, key):
        key = int(key)
        noAtual = self.root
        noSentinela = None
        while noAtual is not None:
            if noAtual.key == key:
                if noAtual.left is None and noAtual.right is None:
                    if noSentinela is None:
                        self.root = None
                        self.size = 0
                    else:
                        if noSentinela.left == noAtual:
                            noSentinela.left = None
                            self.size -= 1
                        elif noSentinela.right == noAtual:
                            noSentinela.right = None
                            self.size -= 1
                elif (noAtual.left is None and noAtual.right is not None) or (noAtual.left is not None and noAtual.right is None):
                    if noSentinela is None:
                        if noAtual.left is not None:
                            self.root = noAtual.left
                            self.size -= 1
                        else:
                            self.root = noAtual.right
                            self.size -= 1
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
            noSentinela = noAtual
            if key < noAtual.key:
                noAtual = noAtual.left
            else:
                noAtual = noAtual.right


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
        noAtual = self.root
        noSentinela = None
        while noAtual is not None:
            # verifica se encontrou o nó a ser removido
            if noAtual.key == key:
                # caso 1: o nó a ser removido não possui filhos (nó folha)
                if noAtual.left is None and noAtual.right is None:
                    # verifica se é a root
                    if noSentinela is None:
                        self.root = None
                        self.size -= 1
                    # verifica se é filho à left ou à right
                    else:
                        if noSentinela.left == noAtual:
                            noSentinela.left = None
                            self.size -= 1

                        elif noSentinela.right == noAtual:
                            noSentinela.right = None
                            self.size -= 1
                # caso 2: o nó a ser removido possui somente um filho
                elif (noAtual.left is None and noAtual.right is not None) or (noAtual.left is not None and noAtual.right is None):
                    # verifica se o nó a ser removido é a root
                    if noSentinela is None:
                        # verifica se o filho de noAtual é filho à left
                        if noAtual.left is not None:
                            self.root = noAtual.left
                            self.size -= 1
                        else: # senão o filho de noAtual é filho à right
                            self.root = noAtual.right
                            self.size -= 1
                    else:
                        # verifica se o filho de noAtual é filho à left
                        if noAtual.left is not None:
                            # verifica se noAtual é filho à left
                            if  noSentinela.left and noSentinela.left.key == noAtual.key:
                                noSentinela.left = noAtual.left
                            else:# senão noAtual é filho à right
                                noSentinela.right = noAtual.left
                        else:# senão o filho de noAtual é filho à right
                            # verifica se noAtual é filho à left
                            if noSentinela.left and noSentinela.left.key == noAtual.key:
                                noSentinela.left = noAtual.right
                            else:# senão noAtual é filho à right
                                noSentinela.right = noAtual.right
                    
                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da subárvore à direita
                elif (noAtual.left is not None) and (noAtual.right is not None):
                    
                    terceiro = noAtual
                    segundo = noAtual.right
                    primeiro = noAtual.right.left
                    
                    while primeiro is not None:
                        terceiro = segundo
                        segundo = primeiro
                        primeiro = segundo.left
                    # verifica se o nó a ser removido é a root
                    if noSentinela is None:
                        # Caso especial: o nó que vai ser a nova root é filho da root
                        if self.root.right.key == segundo.key:
                            segundo.left = self.root.left
                        else:
                            '''
								verifica se o segundo é filho à left ou à right
								para setar para None o segundo
							'''
                            if terceiro.left.key == segundo.key:
                                terceiro.left = None
                            else:
                                terceiro.right = None
                            # seta os filhos à right e left de segundo
                            segundo.left = noAtual.left
                            segundo.right = noAtual.right
                        # faz com que o segundo seja a root
                        self.root = segundo
                    else:
                        '''
							verifica se noAtual é filho à left ou à right
							para setar o segundo como filho do pai do noAtual (noSentinela)
						'''
                        if noSentinela.left.key == noAtual.key:
                            noSentinela.left = segundo
                        else:
                            noSentinela.right = segundo
                        '''
							verifica se o segundo é filho à left ou à right
							para setar para None o segundo
						'''
                        if terceiro.left.key == segundo.key:
                            terceiro.left = None
                        else:
                            terceiro.right = None

						# seta os filhos à right e left de segundo
                        segundo.left = noAtual.left
                        segundo.right = noAtual.right
                break 
            noSentinela = noAtual

            # verifica se vai para left ou right
            if key < noAtual.key:
                noAtual = noAtual.left
            else:
                noAtual = noAtual.right
        return noAtual.value


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

