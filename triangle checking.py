def tcheck()
 x=int(input("Enter Length of First Side "))
 y=int(input("Enter Length of second Side "))
 z=int(input("Enter Length of third Side "))
 flag=0
 if (x+y)<=z:
 flag=0
 elif (x+z)<=y:
  flag=0
elif (y+z)<=x:
  flag=0
else:
   flag=1
if(flag==1):
 print("Yes")
else:
 print("No")