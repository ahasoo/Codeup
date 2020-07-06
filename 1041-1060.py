a = input()
print(chr(ord(a)+1))

a = input().split()
print(int(a[0])//int(a[1]))

a = input().split()
print(int(a[0])%int(a[1]))

a = int(input())
print(a+1)

a = input().split()
print(int(a[0])+int(a[1]))
print(int(a[0])-int(a[1]))
print(int(a[0])*int(a[1]))
print(int(a[0])//int(a[1]))
print(int(a[0])%int(a[1]))
print("%.2f"%(int(a[0])/int(a[1])))

a = input().split()
sum = int(a[0])+int(a[1])+int(a[2])
print(sum)
print(round(sum/3,1))

a = int(input())
print(a<<1)

a = input().split()
print(int(a[0])*(2**int(a[1])))

a = input().split()
if int(a[0])>int(a[1]):
    print("1")
else:
    print("0")

a = input().split()
if int(a[0])==int(a[1]):
    print("1")
else:
    print("0")

a = input().split()
if int(a[0])<=int(a[1]):
    print("1")
else:
    print("0")

a = input().split()
if int(a[0])!=int(a[1]):
    print("1")
else:
    print("0")

a = int(input())
if a == 0:
    print("1")
elif a == 1:
    print("0")

a = input().split()
if int(a[0]) == 1 and int(a[1]) == 1:
    print("1")
else:
    print("0")

a = input().split()
if int(a[0]) == 1 or int(a[1]) == 1:
    print("1")
else:
    print("0")

a = input().split()
if (int(a[0]) == 1 and int(a[1]) == 0) or (int(a[0]) == 0 and int(a[1]) == 1):
    print("1")
else:
    print("0")

a = input().split()
if (int(a[0]) == 1 and int(a[1]) == 1) or (int(a[0]) == 0 and int(a[1]) == 0):
    print("1")
else:
    print("0")

a = input().split()
if int(a[0]) == 0 and int(a[1]) == 0:
    print("1")
else:
    print("0")

a = int(input())
print(~a)

a = input().split()
print(int(a[0])&int(a[1]))
