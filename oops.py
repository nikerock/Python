num = input('Enter the number : ')
y = 0
z = int(num)
while z > 0:
    y += z % 10 ** len(num)
    z /= 10
if int(num) == y:
    print("Armstrong")
else:
    print("not Armstrong")