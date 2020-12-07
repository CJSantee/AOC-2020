lines = 2148
data = []
responces = []

for i in range(lines):
    responces.append([])

numGroups = 0

for loop in range(lines):
    line = input()
    if line == '':
        numGroups += 1
    
    fields = line.split()
    
    for field in fields:
        responces[numGroups].append(set(field))

for i in range(responces.count([])):
    responces.remove([])

count = 0
for i in range(len(responces)):
    intersect = set.intersection(*responces[i])
    count += len(intersect)
    

# count = 0
# for i in responces:
#     count += len(i[0])

print(count)
        
# print(responces)