def perfect_number(x):
  sum=0
  if x>2:
    for i in range(1,x):
     if x%i==0:
       sum=sum+i
    return sum==x
  else:
   return False

x=int(input())
print(perfect_number(x))
  