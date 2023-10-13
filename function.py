def to9(number) -> str:
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[:2])
    else:
        pass
    return number

def to639(number) -> str:
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    return number

def toplus63(number) -> str:
    if str(number[0]) == "0":
        number = "+63"+str(number[1:])
    elif str(number[:2]) == "63":
        number = "+"+str(number)
    else:
        pass
    return number
def to09(number) -> str:
    if str(number[0]) == "+":
        number = "0"+str(number[1:])
    elif str(number[:2]) == "63":
        number = "0"+str(number[2:])
    else:
        pass
    return number
def pick():
    a = input("\033[1;92m╚═════\033[1;91m>>>\033[1;97m")
    return a