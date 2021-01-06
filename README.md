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
  - b = hex(a) #integer to hex  <----> int(b,16) #hex to int


Q. i don't need to care variable size?
As "Python allow you to only take care about variable name and ignore it's
size because pyhton **dynamicly allocate** it so what's the limit in the allocated size in the memory" ??

