lines = 881
seatIDs = []
for loop in range(lines):
    seat = input()
    rowMin = 0
    rowMax = 127
    for i in range(7):
        if seat[i] == 'F':
            rowMax = rowMax - int((rowMax+1-rowMin)/2)
        if seat[i] == 'B':
            rowMin = rowMin + int((rowMax+1-rowMin)/2)
    colMin = 0
    colMax = 7
    for i in range(7, 10):
        if seat[i] == 'L':
            colMax = colMax - int((colMax+1-colMin)/2)
        if seat[i] == 'R':
            colMin = colMin + int((colMax+1-colMin)/2)
    
    seatId = (rowMin * 8)+colMin
    seatIDs.append(seatId)

for i in range(1023):
    if (seatIDs.count(i-1) == 1 and seatIDs.count(i) == 0 and seatIDs.count(i+1) == 1):
        print(i)

