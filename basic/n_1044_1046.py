#21.1.8

#1044
a = int(input())
print(a+1)

#1045

a,b = map(int, input().split(" "))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%0.2f"%(a/b))
# print(round(a/b,2))

#1046

a,b,c = map(int,input().split(" "))
num = [a,b,c]
print(sum(num))
print("%0.1f" % (sum(num)/len(num)))
