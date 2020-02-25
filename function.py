def record(**a):
    if a.get('name') is None and a.get('age') is None and a.get('city') is None:
        print("nothing to store")
    elif a.get('name') is not None and a.get('age') is None and a.get('city') is None:
        print(a.get('name'))
    elif a.get('name') is  None and a.get('age') is not None and a.get('city') is None:
        print(a.get('age'))
    elif a.get('name') is None and a.get('age') is None and a.get('city') is not None:
        print(a.get('city'))
    elif a.get('name') is not None and a.get('age') is not None and a.get('city') is not None:
        print(a.get('name'),a.get('age'),a.get('city'))
    elif a.get('name') is not None and a.get('age') is not None and a.get('city') is None:
        print(a.get('name'),a.get('age'))

#record()
#record(name ="xyz")
#record(age = 25)
#record(city =  "chandigarh")
#record(name ="xyz",age =  25,  city = "chandigarh")
record(name = "xyz",age =  25)
record(age =  25 ,name ="xyz")
#record(city ="chandigarh", age = 25)
#record(city =  "chandigarh", name = "xyz")
#record(age = 25, city = "chandigarh")