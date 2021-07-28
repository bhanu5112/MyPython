#time of the day using time
def timeofthedaywithtime():
  x=int(input("Enter thre time in 24 hr scale"))
  if x<0:
   print("invalid")
  elif x<=5:
   print("Night")
  elif x<=11:
   print("Morning")
  elif x<=17:
   print("Afternoon")
  elif x<=24:
   print("Evening")
  else:
   print("Invalid")
timeofthedaywithtime()