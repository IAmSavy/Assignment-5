Range = [int(input('Enter a range of numbers: ')), int(input())]

for x in range(Range[0], Range[1] + 1):
    Prime_Counter = 0
    for y in range(2, x):
        if x%y == 0: Prime_Counter +=1
    if Prime_Counter == 0 : print(x)