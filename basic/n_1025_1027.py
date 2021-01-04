#21.01.04

#1025

number = input()
for i in range(len(number)):
print('[{}]'.format(int(number[i])*10**(4-i)))

#1026 ; 23:14:23 --> print 'minute'

times = list(input().split(":"))
print(int(times[1]))


#1027 ; make 4 -> 04

dates = list(map(int,input().split(".")))
print("%02d" % dates[2] +"-"+
"%02d" % dates[1]+"-"+ "%04d" % dates[0])
