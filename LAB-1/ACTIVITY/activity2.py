sum=0
s=input("Enter an integer value...")
n=int(s)

while n!=0:
    sum=sum+n
    s=input("Enter an integer value...")
    n=int(s)
    
print("Sum of given values is ",sum)