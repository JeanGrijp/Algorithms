
class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = No(None) 

    def insert(self, value):
        if self.first.value is None: 
            self.first = No(value)
        else:
            aux = self.first 
            while aux.next is not None: 
                aux = aux.next
            aux.next = No(value) 
    
    def remove(self):
        if self.first.value is None: 
            print("Pilha vazia")
        else:
            aux = self.first 
            aux_before = aux 
            while aux.next is not None: 
                aux_before = aux
                aux = aux.next
            aux_before.next = None 

    def show(self):
        if self.first.value is None:
            print("Pilha vazia")
        else:
            aux = self.first
            while aux.next is not None:
                print(aux.value)
                aux = aux.next

