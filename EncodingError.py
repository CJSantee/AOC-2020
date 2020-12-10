lines = 1000
data = []
for loop in range(lines):
    data.append(int(input()))

for num in range(25, lines):
    sumFound = False
    for i in range(num-25, num):
        for j in range(i+1, num):
            # print(data[i], end='')
            # print(" + ", end='')
            # print(data[j], end='')
            # print(" = ", end='')
            # print(data[i] + data[j])
            if(data[i] + data[j] == data[num]):
                sumFound = True
    if(sumFound == False):
        print(data[num])
        break

def sumList(minIndex, maxIndex):
    sum = 0
    for i in range(minIndex, maxIndex):
        sum += data[i]
    return sum

ansList = []
def printSumList(minIndex, maxIndex):
    sum = 0
    for i in range(minIndex, maxIndex):
        print("Sum = ", end='')
        print(sum, end='')
        print(' + ', end='')
        print(data[i], end=' = ')
        sum += data[i]
        ansList.append(data[i])
        print(sum)

    return sum

for i in range(lines):
    for j in range(i+1, lines):
        test = sumList(i, j)
        if(test == 731031916):
            print("FOUND")
            print(i, end=' = ')
            print(data[i])
            print(j-1, end=' = ')
            print(data[j-1])
            print(data[i] + data[j])
            printSumList(i, j)
            print("RESULT: ", end='')
            print(min(ansList) + max(ansList))
        elif(test > 731031916):
            break
