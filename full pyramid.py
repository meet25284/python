row=(int(input("enter no. of value you want to get:"))+1)

for i in range(row):
    print(" " * (row - i),end="")
    print("* " * i)