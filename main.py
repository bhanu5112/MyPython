x=input()
'''x=x.lower()
for i in ',.;!:':
  x=x.replace(i,"")
x=x.split(" ")'''

def freqWords():
  x = ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was','reluctant', 'to', 'open', 'his', 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After', 'the', 'delicious', 'freedom']
  fqwords={}
  for i in x:
    c=x.count(i)
    print(c)
    if c not in fqwords:
      fqwords[c]=[]
     
    if i not in fqwords[c]:
      fqwords[c].append(i)
  return fqwords
print(freqWords())