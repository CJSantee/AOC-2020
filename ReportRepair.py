expenses = []
for i in range(200):
    expense = int(input())
    expenses.append(expense)
for i in expenses:
    for j in expenses:
        for k in expenses: 
            if (i+j+k) == 2020:
                print(i*j*k)