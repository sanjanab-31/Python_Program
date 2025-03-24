l=[1,2,3,4]
l.append(5)
print(l)

l1=[1,2,33,44,51,65]
print(max(l1))


l1=[1,1,2,3,3]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

l2=[1,2,3,4,4,2,4,1,7]
l1=[]
for i in l2:
    if i not in l1:
        l1.append(i)
print(l1)

l1=[1,2,3,4,5]
l2=l1.copy()
print(l2)

l1=['abc', 'xyz', 'aba', '1221']
count=0
for i in l1:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print(count)