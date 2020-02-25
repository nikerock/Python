data = input('enter a charecter : ')
x = ''
for i in data:
    if (ord(i) >= 97 and ord(i) <=122 or ord(i) >= 65 and ord(i) <= 90):
        if (ord(i) != 97 and ord(i) != 101 and ord(i) != 105 and ord(i) != 111 and ord(i) != 117
            and ord(i) != 65 and ord(i) != 69 and ord(i) != 73 and ord(i) != 79 and ord(i) != 90):
            x += i
print(x)