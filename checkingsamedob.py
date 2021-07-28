#n1=input()
dob1=input()
#n2=input()
dob2=input()
#n3=input()
#dob3=input()
dob1=dob1[6:]+"-"+dob1[3:5]+'-'+dob1[:2]
dob2=dob2[6:]+"-"+dob2[3:5]+'-'+dob2[:2]
if dob1>dob2:
  print(dob1)
elif dob1<dob2:
  print(dob2)
else:
  print("same")