class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
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

    def remove(self, value):
        if self.first.value is None:
            return None
        else:
            aux = self.first
            aux_before = aux
            while aux.next is not None:
                if aux.value == value:
                    aux_before.next = aux.next
                    break
                else:
                    aux_before = aux
                    aux = aux.next