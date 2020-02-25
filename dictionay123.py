d = dict()
name =""
age =0
city= ""
mobile=0
i=0
while i< 5:
    name = input('Enter the  name :')
    age = input('Enter the age :')
    city = input("Enter the city:")
    mobile =  input('Enter the phone num:')
    d.update({name:{'age':age,'city':city,'mobile':mobile}})
    i += 1
for i in d:
    print("Name:{}".format(i))
    for j,k in d[i].items():
        print("\t{}\t\t{}".format(j,k))