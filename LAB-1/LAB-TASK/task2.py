even=0
odd=0
for i in range(1,6,1):
    num=int(input("Enter Number: "))
    
    if num%2==0:
        even+=num
    
    else:
        odd+=num
        


print("Sum of Even Numbers: ",even)
print("Sum of Odd Number: ",odd)

