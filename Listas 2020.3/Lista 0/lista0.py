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

def verifyIfNum (string):
    for i in string:
        if ord(i) > 47 and ord(i) < 58:
            return True
    return False

def separa (stringFull):
    text = ""
    middleList = []
    listFinish = []
    for i in stringFull:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            text += i
        elif ord(i) == 44:
                middleList.append(text)
                text = ""
        elif ord(i) == 93:
                middleList.append(text)
                listFinish.append(middleList)
                middleList = []
                text = ""
    return listFinish

def splitLists(stringFull):
    if stringFull is None:
        return None
    else:
        num = ""
        middleList = []
        listFinish = []
        if verifyIfNum(stringFull):
            for i in stringFull:
                if ord(i) > 47 and ord(i) < 58:
                    num += i
                elif ord(i) == 44:
                    middleList.append(num)
                    num = ""
                elif ord(i) == 93:
                    middleList.append(num)
                    listFinish.append(middleList)
                    middleList = []
                    num = ""
            return listFinish
        else:
            return separa(stringFull)

def verifyBiggestList (lists):
    if lists is not None:
        biggest = lists[0]
        for i in range(len(lists)):
            if len(lists[i]) > len(biggest):
                biggest = lists[i]
            if lists[i] == [''] and len(lists) <= 2:
                try:
                    biggest = lists[i+1]
                except:
                    biggest = lists[i-1]
        final = takeSpace(biggest)
        return final
    else:
        return





#lists = input()
a = "[1,2,3]"
b = "[5,6]"




c = "[True,False,False]"
d = "[True,True,True,True]"
e = "[]"

g = "[True]"

lists = a+b
nums = c+d+e+d+g

x = e+g
der = e+e
verifyBiggestList(splitLists(x))
verifyBiggestList(splitLists(der))

verifyBiggestList(splitLists(nums))
#verifyBiggestList(splitLists(lists))
