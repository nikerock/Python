x=[]
a=0
while a<5:
    y=input("Enter the list value")
    for i in x:
        if i== y:
            print("insert again")
            break
    else:
        x.insert(a,y)
        a += 1
print(x)
