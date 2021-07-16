"Diamond" 

user = int(input('Enter Rows: '))

for num in range (1,user+1):
    for i in range(1, user-num+1):
        print (end=" ")
    for i in range(num, 0, -1):
        print(i, end="")
    for i in range(2, num +1):
        print(i, end="")
    print()
aa= user- 1
for i in range(aa, 0, -1):  
    for j in range(user-i):
        print('', end=" ")
    for j in range(i, 0, -1):  
        print(j,end="")   
    for j in range(2, i + 1):  
        print(j , end="")  
    print(" ")  



