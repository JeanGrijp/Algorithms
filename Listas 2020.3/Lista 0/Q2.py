
#123 = {
#125 = }

def takeSpace(string):
    text = ""
    for i in string:
        if ord(i) == 32:
            continue
        else:
            text += i
    return text

def verify (string):
    text = takeSpace(string)
    if text[0] == "}" or text[-1] == "{":
        return "N"
    aux1 = "{"
    aux2 = "}"
    num1 = 0
    num2 = 0
    for i in text:
        if num2 > num1:
            return "N"
        if i == aux1:
            num1 += 1
        elif i == aux2:
            num2 += 1
        else:
            return "N"
    if (num1 - num2) == 0:
        return "S"
    else:
        return "N"

    """
    if text[0] == "}" or text[-1] == "{":
        return "N"
    aux1 = "{"
    aux2 = "}"
    num1 = 0
    num2 = 0
    if len(text) == 2:
        if (text[0] == aux2) and (text[1] == aux1):
            return "N"
        else:
            return "S"
    for i in text:
        if i == aux1:
            num1 += 1
        elif i == aux2:
            num2 += 1
        else:
            return "N"
    if (num1 == num2) and (num1 != 0):
        return "S"
    else:
        return "N"
    """


def menu ():
        
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
    print(verify(string))

certo = "{ { { } } }"
a = "{ } { }"
b = "{ { } } { }"
c = "{ { } { { } { } } }"

d = "{ } {"
e = "{ { } } { } }"
f = "{ } { } }"

asd = "{ } { }"

errado = "{ { } } { { { } }"

print(verify(asd+asd+asd+asd+asd))