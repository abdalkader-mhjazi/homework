d=int(input("Enter decimal number: "))
binary_namber=[]
while(d>0):
    temp = d%2
    binary_namber.append(temp)
    d=d//2
binary_namber.reverse()
print("Equivalent in binary is :", end = " ")
for i in binary_namber:
    print(i,end="")
    
    
    
    
    
    