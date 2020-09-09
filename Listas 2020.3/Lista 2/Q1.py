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
                elif key > no_current.key:
                    no_before = no_current
                    no_current = no_current.right
                    if no_current is None: 
                        no_before.right = No(key, value)
                        self.size += 1
                        cont = False
                elif key == no_current.key:
                    no_current = No(key, value)
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
        no_current = self.root
        no_before = None
        while no_current is not None:
            if no_current.key == key:
                if no_current.left is None and no_current.right is None:
                    if no_before is None:
                        self.root = None
                        self.size -= 1
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
                        # verifica se o filho de no_current é filho à left
                        if no_current.left is not None:
                            # verifica se no_current é filho à left
                            if  no_before.left and no_before.left.key == no_current.key:
                                no_before.left = no_current.left
                            else:# senão no_current é filho à right
                                no_before.right = no_current.left
                        else:# senão o filho de no_current é filho à right
                            # verifica se no_current é filho à left
                            if no_before.left and no_before.left.key == no_current.key:
                                no_before.left = no_current.right
                            else:# senão no_current é filho à right
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
                            menor_no.left = self.root.left
                        else:
                            '''
								verifica se o menor_no é filho à left ou à right
								para setar para None o menor_no
							'''
                            if menor_no_before.left.key == menor_no.key:
                                menor_no_before.left = None
                            else:
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
                            no_before.left = menor_no
                        else:
                            no_before.right = menor_no
                        '''
							verifica se o menor_no é filho à left ou à right
							para setar para None o menor_no
						'''
                        if menor_no_before.left.key == menor_no.key:
                            menor_no_before.left = None
                        else:
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