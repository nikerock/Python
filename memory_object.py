l1 = [1,2,3,4,5]
l2 = ['hello',True,12.5, 101]
l3 = [[1,2,3],['hello',True]]
x=0
for i in l1:
    print("Index{}:{}".format(x,i))
    x +=1
for i in l2:
    print("index{}:{}".format(x,i))

for i,j in enumerate(l2):
    print(i,j)