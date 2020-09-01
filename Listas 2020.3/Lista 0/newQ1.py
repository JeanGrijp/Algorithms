import sys

def getInputs():
    inputs = []
    cont = True
    try:
        while cont:
            inputs.append(input())
    except:
        pass
    return inputs

def splitLists(stringFull):
    # [][Tlista
    # print(lista)
    if stringFull is None:
        return None
    else:
        num = ""
        middleList = []
        listFinish = []
        for i in range(len(stringFull)):
            print(stringFull[i])
            if stringFull[i] == "'" or stringFull[i] == '"':
                continue
            elif stringFull[i] == ",":
                middleList.append(num)
                if stringFull[i+1] == "]" or stringFull[i+1] == "[":
                    num = ""
            elif stringFull[i] == "]":
                num += stringFull[i]
                middleList.append(num)
                listFinish.append(middleList)
                middleList = []
                num = ""
            else:
                num += stringFull[i]
        aux = []
        for i in listFinish:
            # print(i)
            aux.append(i[0])
        return aux

def prin(lista):
    print(lista)
    #lista = getInputs()
    big = lista[0]
    bigLen = 0
    biggest = 0
    for i in lista:
        # print(i)
        if "[" in i and "]" in i:
            aux = i.count(",")
            # print(aux)
            if aux > bigLen:
                bigLen = aux
                biggest = i
    print(biggest)    

"""
def main():
    prin()

if _name_ == '_main_':
    main()
"""


a = "[1,2,3]"
b = "[5,6,12,13]"
we = "[True,True,True,True]"




c = "[True,False,False,True,True]"
d = "[True,True,True,True]"
e = "[]"
f = ""
g = "[True]"
y = "[""]"



x = e+g+e+e+f+y+d

prin(splitLists(x))