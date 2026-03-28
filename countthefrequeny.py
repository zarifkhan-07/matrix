def frequency():
    s=s.lower()
    d={}

    for i in range(len(s)):
        if s[i] in d.keys:
            d[s[i]]+=1
        else:
            d[s[i]]==1
    return d

inp=input("Enter the string")
print(frequency(inp))