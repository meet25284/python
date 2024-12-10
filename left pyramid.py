row=int(input("enter no. of value you want to get:"))

for i in range(1,row + 1):
   print(" " * (row - i),end="")
   print("* " * i)
