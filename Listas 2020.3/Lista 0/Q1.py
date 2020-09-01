def takeSpace (lista):
    string = str(lista) + " "
    text = ""
    final = ""
    for i in string:
        if (ord(i) != 32):
            if(ord(i) != 34):
                if(ord(i) != 39):
                    text += i
                else:
                    final += text
                    text = ""
            else:
                final += text
                text = ""
        else:
            final += text
            text = ""
    return final

def splitLists(stringFull):
    if stringFull is None:
        return None
    else:
        num = ""
        middleList = []
        listFinish = []
        for i in stringFull:
            if ord(i) == 39 or ord(i) == 34 or ord(i) == 91 or ord(i) == 32:
                continue
            elif ord(i) == 44:
                middleList.append(num)
                num = ""
            elif ord(i) == 93:
                middleList.append(num)
                listFinish.append(middleList)
                middleList = []
                num = ""
            else:
                num += i
        return listFinish

def verifyBiggestList (lists):
    if lists is not None:
        biggest = lists[0]
        for i in range(len(lists)):
            if len(lists[i]) > len(biggest):
                biggest = lists[i]
            if lists[i] == ['']:
                try:
                    biggest = lists[i+1]
                except:
                    for j in range(len(lists) -1, 0, -1):
                        if lists[j] != ['']:
                            biggest = lists[j]
                            break
                    #biggest = lists[i-1]
        final = takeSpace(biggest)
        print(final)
        return final
    else:
        return



"""
inputs = []
cont = True
try:
    while cont:
        inputs.append(input())
except:
    pass

string = ""
for i in inputs:
    string += str(i)

print(verifyBiggestList(splitLists(string)))


"""
#lists = input()
a = "[1,2,3]"
b = "[5,6,12,13]"
we = "[True,True,True,True]"




c = "[True,False,False,True,True]"
d = "[True,True,True,True]"
e = "[]"
f = ""
g = "[True]"



x = e+g+e+e+a+c

verifyBiggestList(splitLists(x))