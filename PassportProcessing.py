lines = 1029
data = []
passports = []

for i in range(lines):
    passports.append([])

numPassports = 0

for loop in range(lines):
    line = input()
    if line == '':
        numPassports += 1
    
    fields = line.split()
    
    for field in fields:
        passports[numPassports].append(field)

for i in range(passports.count([])):
    passports.remove([])
    
validHairChar = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
# amb blu brn gry grn hzl oth.
validEyeClr = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
numChars = {'0','1','2','3','4','5','6','7','8','9'}

# numInvalid = 0
numValid = 0
for passport in passports:
    check = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False
    }
    for field in passport:
        pairs = field.split(':')
        key = pairs[0]
        value = pairs[1]
        print(key)
        if(key == 'byr'):
            if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                check["byr"] = True
        if(key == 'iyr'):
            if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                check["iyr"] = True
        if(key == 'eyr'):
            if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                check["eyr"] = True
        if(key == 'hgt'):
            system = value[len(value)-2:len(value)]
            if(system != "cm" and system != "in"):
                break
            num = int(value[0:len(value)-2])
            if(system == "cm" and num >= 150 and num <= 193):    
                check["hgt"] = True
            elif(system == "in" and num >= 59 and num <= 76):    
                check["hgt"] = True
        if(key == 'hcl'):
            checkHair = True
            if value[0] != "#" or len(value) != 7:
                checkHair = False
                break
            for i in range(1, 7):
                if(value[i] not in validHairChar):
                    checkHair = False
            check["hcl"] = checkHair
        if(key == 'ecl'):
            if value in validEyeClr:
                check["ecl"] = True
        if(key == 'pid'):
            checkPID = True
            if len(value) != 9:
                checkPID = False
            for i in value:
                if i not in numChars:
                    checkPID = False
            check["pid"] = checkPID
    
    finalCheck = True
    for x in check:
        if check[x] == False:
            print(passport)
            print("Missing: ", end="")
            print(x)
            finalCheck = False
    if finalCheck == True:
        numValid += 1

print(numValid)