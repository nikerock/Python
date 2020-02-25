data = input('Enter string:')
search = input('Enter character need to be searched:')
y=0
for i in data:
    if search == i:
        y += 1

print(y)