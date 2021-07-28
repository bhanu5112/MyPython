x=input()
depth=0
match=False
maxdep=0
if x.count("(")==x.count(")"):
 match=True
 for i in x:
   if i=="(":
     depth=depth+1
     if depth>maxdep:
       maxdep=depth
   elif i==")":
      depth=depth-1
      if depth==-1:
        match=False
   else:
      pass
if(match):
 print("matched",maxdep)
else:
 print("Unmatched") 