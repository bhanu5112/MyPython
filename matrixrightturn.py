M = []
M1=[]
row = input()
#M_=row.strip().split(" ")
#print (row,type(row))
while row:
    t = row.strip().split(" ")
    M.append(t)
    row = input() 

for i in range(len(M[0])):
  for j in range(len(M)):
   if j== len(M)-1:
     print(M[j][len(M[0])-1-i])
   else:
      print(M[j][len(M[0])-1-i],end=" ")
   