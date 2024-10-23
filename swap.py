def swap(x, y):
        # Swapping the values of a and b
    temp = a
    a = b
    b = temp
    return a, b  # Returning swapped values


# Input from the user
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

# Displaying original values
print(f"Before swapping: x = {x}, y = {y}")

# Calling the swap function
x, y = swap(x, y)

# Displaying swapped values
print(f"After swapping: x = {x}, y = {y}")

