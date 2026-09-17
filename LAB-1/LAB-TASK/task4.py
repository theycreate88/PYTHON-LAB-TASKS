marks=int(input("Enter Marks: "))

if marks<0 or marks>100:
    print("Invalid Range!")
    
else:
    if marks<50:
        print("Grade: F")
    
    elif marks>=50 and marks<=60:
        print("Grade E")
        
    elif marks>=61 and marks<=70:
        print("Grade D")
    
    elif marks>=71 and marks<=80:
        print("Grade C")
        
    elif marks>=81 and marks<=90:
        print("Grade B")
    
    elif marks>=91 and marks<=100:
        print("Grade A")