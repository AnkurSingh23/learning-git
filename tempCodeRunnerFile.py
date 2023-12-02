n=5
for i in range(n):
    for j in range(n):
        if (i==0 and j > 0 and j < 4) or  (j ==0 and i >0  and i < 4)  or (i==4 and j<4 and j > 0)or (j==n-1 and i > 0 and i < 4):
            print("*",end=" ")
        
        
        elif (i==0 and j==0) or (i==4 and j==4) or (i==1 and j==1) or (i==2 and j==2)  or (i==3 and j==3) or (i==0 and j==4) or (i==1 and j==3) or (i==3 and j==1) or (i==4 and j==0):
           print("$",end=" ")
        
        else:
            print(" ",end=" ")
    print()