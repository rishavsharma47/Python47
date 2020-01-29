def insertionSort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        int(">> i[{}] key[{}] j[{}]".format(i, key, j))

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

ages = [12, 34, 11, 67, 88, 77, 37, 43, 51, 13]
insertionSort(ages)

for age in ages:
    print(age, end=" ")


#Orignal Data : 12, 34, 11, 67, 88, 77, 37, 43, 51,13
# i[i], j[0], k]