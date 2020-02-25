data = input('Enter string')
x=''
for ch in data:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
    ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        x += ch

print('the modified string is' , x )