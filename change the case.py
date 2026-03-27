def changecase(s):
    result=""

    for i in s:
        if i.islower():
            result=result+i.upper()
        
        if i.isupper():
            result=result+i.lower()
    return result

inp=input("Enter the word:")

print(changecase(inp))