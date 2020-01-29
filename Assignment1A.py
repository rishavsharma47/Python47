A = [3, 8, 9, 7, 6]

n = 3

# Display original array
print("original A: ")
for i in range(0, len(A)):
    print(A[i], end="")

# Rotate the given array by n times toward right
for i in range(0, len(A)):
    # Stores the last element of array
    last = A[len(A)-1]

    for j in range(len(A)-1, -1, -1):
        # Shift element of array by one
        A[j] = A[j-1]

    # Last element of the array will be added to the start of the array

    A[0] = last


# Display resulting array after rotation
print("Array after right rotatiom: ")
for i in range(0, len(A)):
    print(A[i], end = " ")