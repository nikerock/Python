x = int(input('enter the starting range :'))
y = int(input('Enter the end range :'))

for i in range(x,y+1):
    if (i%2 != 0):
        print(i)