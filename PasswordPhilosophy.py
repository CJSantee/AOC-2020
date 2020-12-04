# numInvalid = 0
# for loop in range(3):
#     lineData = input().split()
#     bounds = lineData[0].split('-')
#     minCount = int(bounds[0])
#     maxCount = int(bounds[1])
#     letter = lineData[1][0:1]
#     count = 0
#     for i in lineData[2]:
#         if i == letter:
#             count += 1
#     if count < minCount or count > maxCount:
#         numInvalid += 1
# print(numInvalid)

# Part 2
numInvalid = 0
numValid = 0
for loop in range(1000):
    lineData = input().split()
    bounds = lineData[0].split('-')
    pos1 = int(bounds[0])
    pos2 = int(bounds[1])
    letter = lineData[1][0:1]
    if lineData[2][pos1-1] == letter:
        if lineData[2][pos2-1] == letter:
            numInvalid += 1
        else:
            numValid += 1
    elif lineData[2][pos2-1] == letter:
        if lineData[2][pos1-1] == letter:
            numInvalid += 1
        else:
            numValid += 1
print(numInvalid)
print(numValid)
