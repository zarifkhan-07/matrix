x=[[8,2,3],[4,1,9],[1,4,8]]

ans=0

for i in range(len(x)):

    for j in range(len(x[0])):
        
        ans=ans+x[i][j]
    
    print(ans,end="")
    ans=0