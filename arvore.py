class No:
    def __init__(self, chave, valor, esquerda = None, direita = None):
        self.chave = chave
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


    def get_chave(self):
        return self.chave

    def set_chave(self, chave):
        self.chave = chave


    def get_esquerda(self):
        return self.esquerda


    def set_esquerda(self, chave):
        self.esquerda = chave

    
    def get_direita(self):
        return self.direita


    def set_direita(self, chave):
        self.direita = chave

    
class Arvore:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0


    def get_raiz(self):
        return self.raiz

    
    def set_raiz(self, chave):
        self.raiz = chave

    
    def get_tamanho(self):
        return self.tamanho

    
    def set_tamanho(self, chave):
        self.tamanho = chave


    def inserir(self, chave, valor):
        cont = True
        no_atual = self.raiz
        no_anterior = None
        if type(chave) == int and type(valor) == str:
            while cont:
                if no_atual is None: #arvore ta vazia
                    self.raiz = No(chave, valor)
                    self.tamanho += 1
                    cont = False
                elif chave < no_atual.chave:
                    no_anterior = no_atual #só pra guardar a referência do No anterior
                    no_atual = no_atual.esquerda# o No atual avança pra esquerda do no anterior
                    if no_atual is None:# se True, é porque o valor que eu quero inserir é menor que o ultimo nó da arvore(folha)
                        no_anterior.esquerda = No(chave, valor) #a importância de guardar a referencia anterior.
                        self.tamanho += 1
                        cont = False
                elif chave > no_atual.chave:# aqui o valor que eu quero inserir é maior que o no atual
                    no_anterior = no_atual
                    no_atual = no_atual.direita
                    if no_atual is None: #se True, o valor que é maior que a folha da arvore.
                        no_anterior.direita = No(chave, valor)
                        self.tamanho += 1
                        cont = False
                elif chave == no_atual.chave: # aqui é pra caso for igual, apenas substituir, outra opção era não fazer nada.
                    no_atual = No(chave, valor)
                    self.tamanho += 1
                    cont = False


    def buscar(self, chave):
        no = self.raiz
        while no is not None:
            if no.chave == chave:
                return no.valor
            elif chave > no.chave:
                no = no.direita
            else:
                no = no.esquerda
        raise KeyError(chave)


    def __len__(self):
        return self.tamanho


    def remover(self, chave):
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
			basta pegar o menor elemento da subárvore à direita
		'''
        chave = int(chave)
        no_atual = self.raiz
        no_anterior = None
        while no_atual is not None:
            # verifica se encontrou o nó a ser removido
            if no_atual.chave == chave:
                # caso 1: o nó a ser removido não possui filhos (nó folha)
                if no_atual.esquerda is None and no_atual.direita is None:
                    # verifica se é a raiz
                    if no_anterior is None:
                        self.raiz = None
                        self.tamanho -= 1
                    # verifica se é filho à esquerda ou à direita
                    else:
                        if no_anterior.esquerda == no_atual:
                            no_anterior.esquerda = None
                            self.tamanho -= 1

                        elif no_anterior.direita == no_atual:
                            no_anterior.direita = None
                            self.tamanho -= 1
                # caso 2: o nó a ser removido possui somente um filho
                elif (no_atual.esquerda is None and no_atual.direita is not None) or (no_atual.esquerda is not None and no_atual.direita is None):
                    # verifica se o nó a ser removido é a raiz
                    if no_anterior is None:
                        # verifica se o filho de no_atual é filho à esquerda
                        if no_atual.esquerda is not None:
                            self.raiz = no_atual.esquerda
                            self.tamanho -= 1
                        else: # senão o filho de no_atual é filho à direita
                            self.raiz = no_atual.direita
                            self.tamanho -= 1
                    else:
                        # verifica se o filho de no_atual é filho à esquerda
                        if no_atual.esquerda is not None:
                            # verifica se no_atual é filho à esquerda
                            if  no_anterior.esquerda and no_anterior.esquerda.chave == no_atual.chave:
                                no_anterior.esquerda = no_atual.esquerda
                            else:# senão no_atual é filho à direita
                                no_anterior.direita = no_atual.esquerda
                        else:# senão o filho de no_atual é filho à direita
                            # verifica se no_atual é filho à esquerda
                            if no_anterior.esquerda and no_anterior.esquerda.chave == no_atual.chave:
                                no_anterior.esquerda = no_atual.direita
                            else:# senão no_atual é filho à direita
                                no_anterior.direita = no_atual.direita
                    
                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da subárvore à direita
                elif no_atual.esquerda is not None and no_atual.direita is not None:
                    
                    menor_no_anterior = no_atual
                    menor_no = no_atual.direita
                    proximo_menor = no_atual.direita.esquerda
                    
                    while proximo_menor is not None:
                        menor_no_anterior = menor_no
                        menor_no = proximo_menor
                        proximo_menor = menor_no.esquerda
                    # verifica se o nó a ser removido é a raiz
                    if no_anterior is None:
                        # Caso especial: o nó que vai ser a nova raiz é filho da raiz
                        if self.raiz.direita.chave == menor_no.chave:
                            menor_no.esquerda = self.raiz.esquerda
                        else:
                            '''
								verifica se o menor_no é filho à esquerda ou à direita
								para setar para None o menor_no
							'''
                            if menor_no_anterior.esquerda.chave == menor_no.chave:
                                menor_no_anterior.esquerda = None
                            else:
                                menor_no_anterior.direita = None
                            # seta os filhos à direita e esquerda de menor_no
                            menor_no.esquerda = no_atual.esquerda
                            menor_no.direita = no_atual.direita
                        # faz com que o menor_no seja a raiz
                        self.raiz = menor_no
                    else:
                        '''
							verifica se no_atual é filho à esquerda ou à direita
							para setar o menor_no como filho do pai do no_atual (no_anterior)
						'''
                        if no_anterior.esquerda.chave == no_atual.chave:
                            no_anterior.esquerda = menor_no
                        else:
                            no_anterior.direita = menor_no
                        '''
							verifica se o menor_no é filho à esquerda ou à direita
							para setar para None o menor_no
						'''
                        if menor_no_anterior.esquerda.chave == menor_no.chave:
                            menor_no_anterior.esquerda = None
                        else:
                            menor_no_anterior.direita = None

						# seta os filhos à direita e esquerda de menor_no
                        menor_no.esquerda = no_atual.esquerda
                        menor_no.direita = no_atual.direita
                break 
            no_anterior = no_atual

            # verifica se vai para esquerda ou direita
            if chave < no_atual.chave:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        return no_atual.valor


    def pre_ordem(self, no):
        if no is None:
            return
        a = "{}:'{}'".format(no.chave, no.valor)
        b = self.pre_ordem(no.esquerda)
        c = self.pre_ordem(no.direita)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string

    def ordem(self, no):
        if no is None:
            return
        b = self.ordem(no.esquerda)
        a = "{}:'{}'".format(no.chave, no.valor)
        c = self.ordem(no.direita)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string


    def pos_ordem(self, no):
        if no is None:
            return
        b = self.ordem(no.esquerda)
        c = self.ordem(no.direita)
        a = "{}:'{}'".format(no.chave, no.valor)
        final_string = a
        if b != None:
            final_string += "->" + str(b) 
        if c != None:
            final_string += "->" + str(c)
        return final_string

