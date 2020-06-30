a = input()
print(a)#1021

a = input()
print(a)#1022

a = input().split(".")
print(a[0])
print(a[1])#1023

a = input()
for i in range(len(a)):
    print("'"+a[i]+"'")#1024

a = int(input())
for j in range(4,-1,-1):
    b = 10**j
    print("["+str((a//b)*b)+"]")
    a -= (a//b)*b#1025

a = input().split(":")
print(int(a[1]))#1026

a = input().split(".")
print("%02d-%02d-%04d"%(int(a[2]),int(a[1]),int(a[0])))#1027

a = int(input())
print(a)#1028

a = float(input())
print("%.11f"%a)#1029

a = int(input())
print(a)#1030

a = int(input())
print("%o" %a)#1031

a = int(input())
print("%x" %a)#1032

a = int(input())
print("%X" %a)#1033

a = "0o"+input()
print(int(a,8))#1034

a = input()
print("%o"%int(a,16))#1035

a = input()
print(ord(a))#1036
#ord = 문자를 아스키코드로

a = int(input())
print(chr(a))#1037
#chr = 아스키코드를 문자로

a = input().split()
print(int(a[0])+int(a[1]))#1038

a = input().split()
print(int(a[0])+int(a[1]))#1039

a = int(input())
print(a*(-1))#1040
