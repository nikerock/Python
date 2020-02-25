x = int(input('Enter the number : '))
if x % 2 == 0:
    x -= 1
else:
    x += 1
for i in range(1,11):
        print(x , 'X' , i , '=' , x*i )