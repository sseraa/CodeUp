#21.1.25

#1066
a = list(map(int,input().split(" ")))
for i in range(len(a)):
  print("even" if a[i]%2==0 else "odd")

#1067
a = int(input())
print("minus" if a<0 else "plus")
print("even" if a%2==0 else "odd")

#1068
a = int(input())
if a>=90:
  print("A")
elif a>=70:
  print("B")
elif a>=40:
  print("C")
else:
  print("D")

#1069
a = input()
if a=="A": print("best!!!")
elif a=="B": print("good!!")
elif a=="C": print("run!")
elif a=="D": print("slowly~")
else: print("what?")

#1070
a = int(input())
if a in (12,1,2): print("winter")
elif a in (3,4,5): print("spring")
elif a in (6,7,8): print("summer")
elif a in (9,10,11): print("fall")
