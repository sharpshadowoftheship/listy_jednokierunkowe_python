class Node:
    def __init__(self):
        self.val=None
        self.next=None



first=None
n=int(input())
for i in range(n):
    k=int(input())
    v=Node()
    v.val=k
    v.next=first
    first=v



find=int(input())
zap=v
print(" ")



f=0

while v!=None:
    if v.val==find:
        print("znaleziono")
        f=1
        break
    else:
        v=v.next

if f==0:
    v=Node()
    v.val=find
    v.next=zap
    first=v

v=first
while v!=None:
    print(v.val)
    v=v.next









