a=[10,20,30,40,50]

a.append(50)
a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(50)
print(a)
a.pop()
print(a)
a.pop(2)
print(a)

a.sort()
print(a)
a.reverse()
print(a)

slice=a[2:5]
print(a,slice)

b=a
print(a,b)
b[0]=99
print(b)
print(a)
c=a.copy()
c=a[:]

a.append(50)
a.append(50)
print(a)
num50=a.count(50)
print(num50)

empty=[]
for val in a:
    if val>=20 and val<=100:
        empty.append(val)
print(empty)

empty=[0]*5
print(empty)
empty[0]=100
print(empty)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares=[val*val for val in range(1,10) if val%2==0]
print(squares)

fav_foods={'kathleen':'tacos','steve':'pizza','sabrina':'pasta',
           'patrick':'chicken','michelle':'pasta'}
print(fav_foods)
food=fav_foods['kathleen']
print(food)
food=fav_foods.get('dan','none')
print(food)

for key,value in fav_foods.items():
    print(key,value)

for key in fav_foods:
    print(key)

if 'Dan' in fav_foods:
    print("Dan's fav food is",fav_foods['Dan'])
else:
    fav_foods['Dan']="cookies"
print(fav_foods)

aset={}
aset=set()
aset.add(1)
aset.add(2)
aset.add(3)
aset.add(3)
print(aset)
no_dups=set([1,1,1,2,2,3,3,3])
print(no_dups)




