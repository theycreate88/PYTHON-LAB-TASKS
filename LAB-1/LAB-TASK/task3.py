num=int(input("Enter Number of terms: "))

num1=0
num2=1

print(num1)
print(num2)
for i in range(1,num-1,1):
    
    num3=num1+num2
    print(num3)
    
    num1=num2
    num2=num3
    