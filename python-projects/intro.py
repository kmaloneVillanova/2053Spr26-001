print("Hello World!")
# this is a comment like //
'''
this is like
/*
comment line
*/
'''

x=100
y=5.5
x="hello"
print(x)

x=100+1
x=100/10
print(int(x))
print(x)
x=100//10
print(x)
x=101%10
min_val=min([1,2,3,4,5])
print(min_val)

x=2**4
x=pow(2,5)

if x>10:
    x=5
    y=10

if x>10 and y<5:
    print("x greater than 10")
    y=10

if x>10 or y==10:
    print("10")

if x < 0:
    x=0
elif x > 10:
    x=0
else:
    x=100

for i in range(5):
    print(i)

lst=[1,2,3,4,5]
for i in range(1,len(lst)):
    print(i,lst[i])

for i, num in enumerate(lst):
    print(i,num)

for val in lst:
    print(val)
num=0
while num < 10:
    print(num)
    num+=1

def hello():
    print("Hello World")
hello()

def greeting(name="Alice"):
    print("Hello", name)
greeting("Bob")
greeting()

demo="Kathleen's email address is"
email='kathleen@gmail.com'

for c in demo:
    print(c)
first_char=email[0]
last_char=email[-1]
print(last_char)

domain=email[9:]
username=email[:9]
print(domain)