
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
    aux1 = "{"
    aux2 = "}"
    num1 = 0
    num2 = 0
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

errado = "{ { } } { { { } }"

print(verify(certo))
print(verify(a))
print(verify(b))
print(verify(c))
print()
print()
print()
print(verify(d))
print(verify(e))
print(verify(f))
print(verify(errado))