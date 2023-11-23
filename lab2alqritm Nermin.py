n=10                                                                                        
a=[0]*n
k=0
from random import randint
for i in range(n):                                                                  
    a[i]=randint(-10,20)
print(a)
cem=0
saygac=0

for i in range(n):
    cem+=a[i]
    
    saygac+=1

ededi_orta=cem/saygac

print(ededi_orta)