lines = 594
rules = []
for loop in range(lines):
    rules.append(input())

count = 0
queue = []
validBags = set()

rulesDict = {}
for rule in rules:
    prefix = rule[0:rule.find('contain')-6]
    suffix = rule[rule.find('contain')+8:len(rule)-1]
    bags = suffix.split(',')
    if(len(bags)>1):
        for i in range(1, len(bags)):
            bags[i] = bags[i][1:len(bags[i])]
    for i in range(len(bags)):
        if(bags[i].find('bags') != -1):
            bags[i] = bags[i][0:len(bags[i])-5]
        else:
            bags[i] = bags[i][0:len(bags[i])-4]
    rulesDict.update({prefix:bags})

# print(rulesDict)

def countBags(searchBag, count):
    bags = rulesDict.get(searchBag)
    if(bags[0] == 'no other'):    
        return 0
    else:
        bagCount = 0
        for bag in bags:
            bagCount += int(bag[0])
            bagCount += int(bag[0]) * countBags(bag[2:len(bag)], count)
        count += bagCount
    
    return count

print(countBags('shiny gold', 0))


# FOR PART 1: 

# for rule in rules:
#     prefix = rule[0:rule.find('contain')-6]
#     suffix = rule[rule.find('contain')+7:len(rule)]
#     if suffix.find('shiny gold') != -1:
        
#         validBags.add(prefix)
#         # print(prefix)
#         queue.append(prefix)
#         count += 1

# while(len(queue) != 0):
#     testBag = queue.pop()
#     for rule in rules:
#         suffix = rule[rule.find('contain')+7:len(rule)]
#         if suffix.find(testBag) != -1:
#             prefix = rule[0:rule.find('contain')-6]
#             if(prefix not in validBags):
#                 # print(prefix)
#                 queue.append(prefix)
#                 validBags.add(prefix)
#                 count += 1

# # print(validBags)
# print(count)

# # print(rules)