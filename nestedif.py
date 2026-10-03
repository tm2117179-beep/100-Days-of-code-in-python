num=int(input("enter the num: "))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 0 to 10")
    elif(num>10 and num<=20):
        print("number is betwen 10 to 20")
    else:
        print("number is positive")  
else:
    print("number is zero")               
