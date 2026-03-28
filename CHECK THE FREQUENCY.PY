test_dict={'Codingal':2, 'Munna':2, 'Lol':3, 'jwbd':3, 'ejf':4,}
print(test_dict)
n=int(input("Enter the number:"))
fre=0
for key in test_dict:
    if test_dict[key]==n:
        fre=fre+1
print(fre)