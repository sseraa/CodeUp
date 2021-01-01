#1022

string = input()
print(string)

#1023
# map(a,b)
#f,b = input().split(".") #what diff?
f,b = map(str,input().split("."))
print(f,b,sep="\n")
print(type(f))

#1024
string = input()
for i in range(len(string)):
  print("'"+string[i]+"'")

