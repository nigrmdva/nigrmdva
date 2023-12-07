import random
def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j],end='    ')
        print()

p=0
n=4
m=4
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(2,6))
printList(a)
print()
for i in range(n):
    p=0
    if (i+1) % 2==0:
        for j in range(m):
                p=p+a[i][j]
        print(i+1,"-ci setrdeki elementlerin hasili:", p)
    else:
        print("\n")