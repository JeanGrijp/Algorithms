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
                        if no_current.left is not None:
                            if  no_before.left and no_before.left.key == no_current.key:
                                no_before.left = no_current.left
                            else:
                                no_before.right = no_current.left
                        else:
                            if no_before.left and no_before.left.key == no_current.key:
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