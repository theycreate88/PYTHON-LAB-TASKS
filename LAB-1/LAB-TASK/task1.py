num=int(input("Enter a Number: "))

num2=num
rev=0
while num>0:
    rev=rev*10
    rev=rev+ num%10
    num=num//10
    

print("Revese: ",rev)