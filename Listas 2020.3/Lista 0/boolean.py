

def verifyIfNum (string):
    for i in string:
        if ord(i) > 47 and ord(i) < 58:
            return True
    return False


def splitLists(stringFull):
    print(stringFull)
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
        print(listFinish)
        print(type(listFinish))
        return listFinish

a = "[1,2,3]"
b = "[5,6,12, 13]"
we = "[True,True,True,True]"




c = "[True,False,False,True,True]"
d = "[True,True,True,True]"
e = "[]"
f = ""
g = "[True]"



x = b+c

splitLists(x)