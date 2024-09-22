num = int(input("Enter any number: "))#first takes input in int value

if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:#apply if else condition
    print("It is not a prime number")
elif num == 1:
    print("1 is not cosider as prime number")
else :
    print("its a prime number")

print(type(num)) #ask to python for object type   