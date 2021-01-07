#21.1.7

#1035
a = input()
print(format(int(a,16),'o'))
int('11',2)#2진수 11 to 10진수

#1036
# chr() <--> ord()
print(ord(input()))

#1037
#chr(int) ; return ascii code
print(chr(int(input())))

#1038
a = input().split(" ")
print(eval(a[0]+"+"+a[1]))

#1039
a = input().split(" ")
print(eval(a[0]+"+"+a[1]))

#1040
print(-int(input()))

#1041
print(a//b)
# a//b --> 몫
# a%b --> 나머지

#1042
a,b= map(int,input().split(" "))
print(divmod(a,b)[1])
# print(a%b)#ord(str); return int
print(chr(ord(input())+1))

#1042
a,b= map(int,input().split(" "))
print(divmod(a,b)[0])
