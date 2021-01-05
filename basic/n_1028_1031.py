#21.1.5

#1028
a = int(input()) #str로 처리 가능
print(a)

'''
Python 수치자료형 범위 @출처:https://joochang.tistory.com/47
1.int(32bit)
  (-2147483648 ~2147483647)
2. long( infinite) ; as long as memory allowing
3. float(64bit)
  (10*E-308 ~ 10*E308, 유효 15자리)
4. complex(실수부,허수부 각가 64bit)
  (10*E-308 ~ 10*E308, 유효 15자리)

* 
32-bit: the value will be 2^31 – 1, i.e. 2147483647
64-bit: the value will be 2^63 – 1, i.e. 9223372036854775807

'''

#1029
a = float(input())
print("%0.11f" % a)

#1030

a = str(input()) # int works
print(a)

#1031
#8진수(e.g 0o177)=0O177), 16진수(e.g. 0x8ff) 사용 잘 안됨
a = int(input())
print("%o" % a) #octal 8진수
