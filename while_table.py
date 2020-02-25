y = 0
while True:
    choice = input('Do you want to continue Y/N Y/y N/n :').lower()
    if (choice =='y'):
        while True:
            y = 0
            x = input('Enter the number : ')
            if x.isnumeric():
                for i in range (1 ,11):
                    print(x , 'X' , i , '=' , int(x)*i)
                break
            else:
                print("Didn't enter number.")
                continue
    elif (choice == 'n'):
        break
    else:
        if y == 2:
            break
        y += 1
        print("invalid")