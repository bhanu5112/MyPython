x=input()
x=x.lower()
for i in ',.;!:':
  x=x.replace(i,"")
x=x.split(" ")

def freqWords():
  fqwords={}
  for i in x:
    c=x.count(i)
    if c not in fqwords:
      fqwords[c]=[]
    if i not in fqwords[c]:
      fqwords[c].append(i)
  return fqwords
print(freqWords())