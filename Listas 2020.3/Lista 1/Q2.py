
class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class Playlist:
    def __init__(self):
        self.first = No("...")

    def insert(self, value):
        if self.first.value == "...":
            self.first = No(str(value))
        else:
            aux = self.first
            while aux.next is not None:
                aux = aux.next
            aux.next = No(value)

    def next(self):
        if self.first.value == "...":
            pass
        elif self.first.next is None:
            self.first = No("...")
        else:
            aux = self.first
            self.first = aux.next

    def play(self):
        if self.first.value == "...":
            print("...")
        else:
            aux = self.first
            print(aux.value)
            self.next()






def main():
    inputs = []
    comands = []
    cont = True
    try:
        while cont:
            inputs.append(input())
    except:
        pass



    playlist = Playlist()


    for i in inputs:
        if i == "\\play":
            playlist.play()
        elif i == "\\next":
            playlist.next()
        else:
            playlist.insert(i)


if __name__ == '__main__':
    main()

