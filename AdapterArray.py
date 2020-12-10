lines = 90
adapters = []
for loop in range(lines):
    adapters.append(int(input()))

adapters.append(0)
adapters.sort()
adapters.append(adapters[len(adapters)-1]+3)
print(adapters)
print(adapters[-2])
combos = 1
for i in range(1, len(adapters)-2):
    if(adapters[i]<=adapters[i-1]+3 and adapters[i+1]<=adapters[i]+3):
        combos = combos * 2
for i in range(2, len(adapters)-3):
     if(adapters[i+2]<=adapters[i-1]+3 and adapters[i+1]<=adapters[i+2]+3 and adapters[i]<=adapters[i+1]+3 and adapters[i+3]<=adapters[i]+3):
        combos = combos + 1

print(combos)

for i in adapters[:]:
    print(i)