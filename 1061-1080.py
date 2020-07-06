a = input().split()
print(int(a[0])|int(a[1]))

a = input().split()
print(int(a[0])^int(a[1]))

a = input().split()
result = a[0] if int(a[0])>int(a[1]) else a[1]
print(result)

a = input().split()
x = a[0] if int(a[0])<int(a[1]) else a[1]
y = x if int(x)<int(a[2]) else a[2]
print(y)

a = input().split()
for i in a:
    if int(i)%2 == 0:
        print(i)

a = input().split()
for i in a:
    if int(i)%2 == 0:
        print("even")
    else:
        print("odd")

a = int(input())
if a > 0:
    print("plus")
else:
    print("minus")
if a % 2==0:
    print("even")
else:
    print("odd")

a = int(input())
if a >= 90:
    print("A")
elif a>=70:
    print("B")
elif a>=40:
    print("C")
else:
    print("D")

a = input()
if a =="A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

a = int(input())
win = [12,1,2]
spr = [3,4,5]
summ = [6,7,8]
fal = [9,10,11]
if a in win:
    print("winter")
elif a in spr:
    print("spring")
elif a in summ:
    print("summer")
elif a in fal:
    print("fall")

a = input().split()
for i in a:
    if int(i) != 0:
        print(i)
    else:
        break

a = input()
b = input().split()
for i in b:
    print(i)

a = input().split()
for i in a:
    if int(i) != 0:
        print(i)
    else:
        break

a = int(input())
for i in range(a,0,-1):
    print(i)

a = int(input())
for i in range(a-1,-1,-1):
    print(i)

a = input()
x = ord('a')
for i in range(x,ord(a)+1):
    print(chr(i),end = " ")

a = int(input())
for i in range(a+1):
    print(i)

sum = 0
a = int(input())
for i in range(a+1):
    if i % 2 == 0:
        sum += i
print(sum)

a = input().split()
for i in a:
    print(i)
    if i == 'q':
        break

a = int(input())
sum = 0
num = 1
while True:
    sum += num
    if sum>=a:
        print(num)
        break
    num += 1
