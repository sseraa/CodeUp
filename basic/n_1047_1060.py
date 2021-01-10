#1047
a = int(input())
print(a<<1)# 2**n

#1048
a,b = map(int,input().split(" "))
print(a<<b)

#1049
a,b = map(int,input().split(" "))
print(1 if a>b else 0)

#1050
a,b = map(int,input().split(" "))
print(1 if a==b else 0)

#1051
a,b = map(int,input().split(" "))
print(1 if a<=b else 0)

#1052
a,b = map(int,input().split(" "))
print(1 if a!=b else 0)

#1053
a = int(input())
print(0 if bool(a) else 1)
# if bool(a): #1 True, 0 False
#   print(0)
# else:
#   print(1)

#1054
a,b = map(int,input().split(" "))
print(1 if (bool(a) & bool(b)) else 0)

#1055
a,b = map(int,input().split(" "))
print(1 if (bool(a) | bool(b)) else 0)

#1056
a,b = map(int,input().split())
print(1 if a^b else 0)
'''
"exclusive or"
If the bits are different, XOR outputs 1.
'''

#1057
#a ^ b <---> ~(a ^ b)
a,b = map(int,input().split())
print(1 if not (a^b) else 0)
#print(1 if ~(a^b) else 0)

#1058
a,b = map(int,input().split())
print(1 if not(a==0 ^ b==0) else 0)
print(1 if not(a|b) else 0)
print(1 if a==b else 0)
why its true????

'''
** 비트단위(bitwise) 연산자는,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
'''
#1059
#~(bitwise not) : tilde
a = int(input())
print(~a)

#1060
# a&b ; bitwise and
# both 1 --> 1 else 0
a,b = map(int,input().split(" "))
print(a&b) #and, ampersand
'''
using when two computer send their date each other, to check whether they are in same network.
+masking 연산
'''
