def swap(s):
    a = ""
    for char in string1:
        if char.isupper() == True:
            a+=(char.lower())
        else:
            a+=(char.upper())
    return a

string1 = input("input your string: \n>")
print(swap(string1))
