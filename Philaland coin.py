Test_cases=int(input())
for i in range (1,Test_cases+1):
  n= int(input())
  count=0
  while n>0:
    n=n//2
    count+=1

  print(count)


#Alternative 

Test_cases=int(input())
for i in range (1,Test_cases+1):
  print (len("{0:b}".format(int(input()))))

# alternate { any number can be represented as the powers two therefore minimum number of denomination required are log2(n)+1 }

from math import log2,floor

print (floor(log2(int(input()))+1))
