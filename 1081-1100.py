a = input().split()
for i in range(int(a[0])):
    for j in range(int(a[1])):
        print(i+1,j+1)

a = int(input(),16)
for i in range(15):
    print("%X*%X=%X"%(a,i+1,a*(i+1)))

a = int(input())
for i in range(a):
    if (i+1)%3 != 0:
        print(i+1,end = " ")
    else:
        print("X",end = " ")

a = input().split()
for i in range(int(a[0])):
    for j in range(int(a[1])):
        for k in range(int(a[2])):
            print(i,j,k)
print(int(a[0])*int(a[1])*int(a[2]))

a = input().split()
a_result = int(a[0])*int(a[1])*int(a[2])*int(a[3])
print(round(a_result/(8*1024*1024),1), "MB")

a = input().split()
a_result = int(a[0])*int(a[1])*int(a[2])
print("%.2f MB"%round(a_result/(8*1024*1024), 2))

a = int(input())
sum = 0
num = 1
while True:
    sum += num
    if sum>=a:
        print(sum)
        break
    num += 1

a = int(input())
for i in range(a):
    if (i+1)%3 != 0:
        print(i+1,end = " ")

a = input().split()
a_ = int(a[0])
d = int(a[1])
n = int(a[2])
print(a_+((n-1)*d))

a = input().split()
a_ = int(a[0])
r = int(a[1])
n = int(a[2])
print(a_*r**(n-1))

a = input().split()
a_ = int(a[0])
m = int(a[1])
d = int(a[2])
n = int(a[3])
for i in range(n-1):
    x = a_*m+d
    a_ = x
print(x)

a = input().split()
num = 2
while True:
    if num%int(a[0])==0 and num%int(a[1])==0 and num%int(a[2])==0:
        print(num)
        break
    else:
        num += 1

a = int(input())
b = input().split()
for i in range(1,24):
    print(b.count(str(i)),end = " ")

a = int(input())
b = input().split()
for i in range(a):
    print(b[a-i-1],end = " ")

a = int(input())
b = input().split()
min = int(b[0])
for i in range(a):
    if int(b[i])<min:
        min = b[i]
print(min)

a = int(input())
board = [[0]* 19 for z in range(19)]#2차원 배열 초기화
putdoll = []
for i in range(a):
    putdoll.append(input().split())
for j in range(len(putdoll)):
    for k in range(2):
        if k == 0:
            x = int(putdoll[j][k])-1
        elif k == 1:
            y = int(putdoll[j][k])-1
    board[x][y] = 1
for p in range(19):
    for q in range(19):
        print(board[p][q], end = " ")
    print()


board = []
for i in range(19):
    board.append(input().split())
num = int(input())
for j in range(num):
    x,y = input().split()
    
    for k in range(19):

        if board[int(x)-1][k] == str(0):
            board[int(x)-1][k] = str(1)
        elif board[int(x)-1][k] == str(1):
            board[int(x)-1][k] = str(0)
            
        if board[k][int(y)-1] == str(0):
            board[k][int(y)-1] = str(1)
        elif board[k][int(y)-1] == str(1):
            board[k][int(y)-1] = str(0)

for p in range(19):
    for q in range(19):
        print(board[p][q], end = " ")
    print()


board = []
w,h = input().split()
for a in range(int(w)):
    board.append([])
    for b in range(int(h)):
        board[a].append(0)
        
num = int(input())
for i in range(num):
    lens,dirc,x,y = input().split()

    for j in range(int(lens)):
        if dirc == "0":
            board[int(x)-1][int(y)-1+j] = 1
        elif dirc == "1":
            board[int(x)-1+j][int(y)-1] = 1

for p in range(int(w)):
    for q in range(int(h)):
        print(board[p][q], end = " ")
    print()



maze = []
for i in range(10):
    maze.append(input().split())
    
x = 1
y = 1

for i in range(30):
    if maze[x][y] == '2':
        maze[x][y] = '9'
        break
    else:
        maze[x][y] = '9'

    if maze[x][y+1] == '1' and maze[x+1][y] == '1':
        break
    
    if maze[x][y+1] != '1':
        y += 1
    elif maze[x+1][y] != '1':
        x += 1
        

for p in range(10):
    for q in range(10):
        print(maze[p][q], end = " ")
    print()
