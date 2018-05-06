x = raw_input()
length = len(x)
digit = 0
letters = 0
space = 0
other = 0
for i in x:
  
  if i.isalpha():
    
    letters += 1
  elif i.isdigit():
    digit += 1
  elif i.isspace():
    space += 1
  else:
    other += 1
    
print other-1    
  
