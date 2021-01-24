#1061
# a or b 1 --> 1
a,b = map(int,input().split(" "))
print(a|b) #or, pipe

#1062
# xor; 서로 다를 때 1
a,b = map(int,input().split(" "))
print(a^b) #xor
'''e.g. 그래픽 이미지, 
색이 서로 다른 부분만 처리'''

#1063
a,b = map(int,input().split(" "))
print(a if a>b else b)

#1064
a,b,c = map(int,input().split(" "))
print(min(a,b,c))

#1065
a,b,c = map(int,input().split(" "))
if a%2==0:
  print(a)
if b%2==0:
  print(b)
if c%2==0:
  print(c)
