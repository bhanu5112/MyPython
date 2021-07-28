number = input()
valid = True
if len(number) == 10 and number.isdigit() == True and number[0] in '6789':
 for digit_index in range(0,5):
  count = number.count(number[digit_index])
  if count > 7:
   valid = False
   break
  if 6*number[digit_index] in number:
   valid = False
   break

else:
 valid=False
if valid == True:
 print("valid")
else:
 print('invalid')