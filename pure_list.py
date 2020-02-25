l = [1,2,5,11,7,9,8,10,12,15,17,12,1,2,3,4,12,11,17,18,19,20,21,1,2,5,7,9,11,12,23,5,6,7,25,91]

y=len(l)
i=0
counter = 0
while i<y:
    if l.count(l[i]) == 1:
        i += 1
        counter += 1
        continue
    else:
        x = l.index(l[i], i+1, y)
        l.pop(x)
        y = len(l)
        i = i
        counter += 1
print(l, counter)