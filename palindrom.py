data = input('Enter a Number :')
x = ''
for i in data:
    x = i + x
if data == x:
    print('it is a palindrom.')
else:
    print('It is not a palindrom.')

