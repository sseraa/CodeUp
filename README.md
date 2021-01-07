### CodeUp

:blossom: **Python 100제** (https://www.codeup.kr/problemsetsol.php?psid=23)

# 자주 헷갈리는 문법 PYTHON GRAMMERS :grimacing:
<br>

1. Input-Output
  - a.zfill(3) # a의 문자를 n개로 만듦 ('2'-> '002')
  - format(a,'03') # a가 정수 일 경우 (2 -> 002)
  - input().split(".")
  - y,m,d = map(str,input().split(".")) # ?? map??
  - dates = list(map(int,input().split("."))
  - print("%o" %a) #int -> octal(8진수)
    == format(a, 'x') == oct(a)
  - b = hex(a) #integer to hex  <----> int(b,16) #hex to int (b must to be str)
    - int('11',2)#2진수 11 to 10진수


<br>
**Knowledge**
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

<br>

Q. i don't need to care variable size?
As "Python allow you to only take care about variable name and ignore it's
size because pyhton **dynamicly allocate** it so what's the limit in the allocated size in the memory" ??

