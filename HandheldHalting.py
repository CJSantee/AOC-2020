lines = 656
commands = []
for loop in range(lines):
    commands.append([input(), False])

minTested = 0
while(commands[len(commands)-1][1] == False):
    for i in range(minTested+1, len(commands)):
        if(commands[i][0][0:3] == 'jmp'):
            val = commands[i][0][3:len(commands[i][0])]
            nop = "nop"
            newString = nop + val
            commands[i][0] = newString
            print("value changed at: ", end='')
            print(i)
            minTested = i
            break
        if(commands[i][0][0:3] == 'nop'):
            val = commands[i][0][3:len(commands[i][0])]
            jmp = "jmp"
            newString = jmp + val
            commands[i][0] = newString
            print("value changed at: ", end='')
            print(i)
            minTested = i
            break
    
    acc = 0
    index = 0
    command = commands[index]
    while(command[1] == False):
        sig = command[0][0:3]
        value = int(command[0][3:len(command[0])])
        if sig == 'acc':
            acc += value
            command[1] = True
            index += 1
        if sig == 'jmp':
            command[1] = True
            index += value
        if sig == 'nop':
            index += 1
        if(index >= len(commands)):
            print(index)
            command[1] = True
        else:
            command = commands[index]

    print(acc)

    for i in range(0, len(commands)-1):
        commands[i][1] = False
    if(commands[minTested][0][0:3]=='jmp'):
        val = commands[minTested][0][3:len(commands[minTested][0])]
        nop = "nop"
        newString = nop + val
        # print(newString)
        commands[minTested][0] = newString
        print("value changed back at: ", end='')
        print(minTested)
    elif(commands[minTested][0][0:3]=='nop'):
        val = commands[minTested][0][3:len(commands[minTested][0])]
        jmp = "jmp"
        newString = jmp + val
        # print(newString)
        commands[minTested][0] = newString
        print("value changed back at: ", end='')
        print(minTested)
    if(minTested == 655):
        break
        
# print(commands)
# print(commands)