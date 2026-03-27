def rev(s):
    return s[::-1]

def pal(s):
    s=s.lower()
    rev_string=rev(s)

    if s==rev_string:
        return True
    else:
        return False
inp=input("Enter string:")
print(pal(inp))
