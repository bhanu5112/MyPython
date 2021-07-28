x=input().lower()
y=['a','b','c','d','e','f','g','h','i',"j",'k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
z=[]
c=0
for i in y:
  for j in range(0,len(x)):
    if(i==x[j]):
     z=z+ [i]
for i in z:
 print(i,end='')