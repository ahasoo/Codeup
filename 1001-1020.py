print("Hello")#1001

print("Hello World")#1002

print("Hello\nWorld")#1003

print("'Hello'")#1004

print('"Hello World"')#1005

print('"!@#$%^&*()"')#1006

print('"C:\Download\hello.cpp"')#1007

print("\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518")#1008
#파이썬에서는 3.0 아래 버전에서는 유니코드 출력x, 아래 문장 삽입해야함
#import io, sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a = int(input())
print(a)#1010

a = input()
print(a)#1011
 
a = float(input())
print("%f" %a)#1012
#%f는 무조건 소수점 아래 6자리까지 맞춰서 출력
#소수점 아래 n자리 출력하려면 %.nf

a = input().split()
print(a[0],a[1])#1013

a = input().split()
print(a[1],a[0])#1014

a = float(input())
print("%.2f"%a)#1015

a = int(input())
print(a,a,a)#1017

a = input()
print(a)#1018

a = input().split('.')
print("%04d"%int(a[0]),"%02d"%int(a[1]),"%02d" %int(a[2]),sep = ".")#1019
#포맷팅할 때는 ""당 %하나

a = input().split('-')
print(a[0]+a[1])#1020
