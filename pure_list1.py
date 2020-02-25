#l = [1,2,5,11,7,9,8,10,12,15,17,12,1,2,3,4,12,11,17,18,19,20,21,1,2,5,7,9,11,12,23,5,6,7,25,91]
l = list(range(10000))
while True:
    length = len(l)
    for i in l:
        occure = l.count(i)
        if occure>1:
            fi = l.index(i)
            si = l.index(i,fi+1)
            l.pop(si)
            break
    if length == len(l):
        break
print(l)