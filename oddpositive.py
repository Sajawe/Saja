number = int(input("Enter a number: "))

if(number %2) == 0:
    print("{0} is even number".format(number))
else:
    print("{0} is odd number".format(number))

if number>0:
    print(number,"is a positive number")
elif number<0:
    print(number,"is a negative number")   
else:
    print("entered number is zero!")
