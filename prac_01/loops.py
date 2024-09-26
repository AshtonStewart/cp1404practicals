
looptype = float(input('Please make your choice here'));

#prints every odd number between 0 and 20
if looptype == 1:
    for i in range(1, 21, 2):
        print(i, end=' ')
#prints every 10th number between 0 and 100 (including 100)
elif looptype == 2:
    for i in range(0, 101, 10):
        print(i, end=' ')
#prints a specified amount of rows. Each row has a 1 more asterisk than the last
elif looptype == 3:
    n = int(input('Specify the number of "*" you wish to print'));
    for i in range(0, n + 1, 1):
        print("*" * i, end='\n')
#prints a countdown from 20 to 1 in increments of 1
elif looptype == 4:
    for i in range (20, 0, -1):
        print(i, end=' ')
#accounts for incorrect inputs
else:
    print("invalid input, please input something else")