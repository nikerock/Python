char = input('Enter a char : ')
if(65<= ord(char) <=90):
    for i in range(ord(char) , 91):
        print(chr(i))
elif(97<= ord(char) <= 122):
    for i in range(ord(char) , 123):
        print(chr(i))