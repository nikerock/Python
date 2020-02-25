num = input('Enter the number : ')
x = 0
for i in num:
    x += int(i) ** len(num)
if int(num) == x:
       print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")