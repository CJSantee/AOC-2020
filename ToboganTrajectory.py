mapData = []
for i in range(323):
    line = input()
    mapData.append([line[j] for j in range(31)])

i = 2
j = 1
count = 0
print(mapData[i][j%31])
while(i < 323):
    if mapData[i][j%31] == "#":
        count += 1
    i += 2
    j += 1
print(count)

# for i in range(31):
#     print(mapData[0][i], end="")


# 58
# 209
# 58
# 64
# 35
print(58*209*58*64*35)