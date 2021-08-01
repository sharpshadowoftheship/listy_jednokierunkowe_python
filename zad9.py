class Node:
    def __init__(self):
        self.val=None
        self.next=None


n=int(input())
first=None

for i in range(n):
    k=int(input())
    v=Node()
    v.val=k
    v.next=first
    first=v


print(" ")



first2=None


while v!=None:
    odwru=Node()
    odwru.val=v.val
    odwru.next=first2
    first2=odwru
    v=v.next


while True:
    if odwru.val+1<10:
        odwru.val+=1
        break
    else:
        odwru.val=0
    if odwru.next!=None:
        odwru=odwru.next
    else:
        zap=odwru
        odwru=Node()
        odwru.val=1
        zap.next=odwru
        break

odwru=first2

while odwru!=None:
    print(odwru.val)
    odwru=odwru.next

#odwrocic liste









