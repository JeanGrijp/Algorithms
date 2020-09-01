class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class Diretorio:
    def __init__(self):
        self.first = No("\\")

    def insert(self, value=None):
        if self.first.value == "\\":
            self.first = No(str(value))
        else:
            aux = self.first
            while aux.next is not None: 
                aux = aux.next
            aux.next = No(str(value))
    
    def remove(self):
        if self.first.value == "\\":
            self.first = No("\\")
        elif self.first.next is None:
            self.first = No("\\")
        else:
            aux = self.first
            aux_before = aux
            while aux.next is not None:
                aux_before = aux
                aux = aux.next
            aux_before.next = None

    def show(self):
        if self.first.value == "\\":
            print("\\")
        else:
            text = ""
            aux = self.first
            while aux.next is not None:
                text += "\\" + str(aux.value)
                aux = aux.next
            text += "\\" + str(aux.value)
            print(text)








def main():
    inputs = []
    cont = True
    try:
        while cont:
            inputs.append(input())
    except:
        pass
    diretorio = Diretorio()
    aux2 = inputs[0].split("\\")
    for i in aux2:
        if i == "":
            continue
        diretorio.insert(i)
    for i in inputs:
        if i[0] == 'c' and i[1] == 'd' and i[2] == " " and i[3] != ".":
            aux = i[3::]
            diretorio.insert(aux)
        elif i == "pwd":
            diretorio.show()
        elif i == "cd ..":
            diretorio.remove()

if __name__ == '__main__':
    main()