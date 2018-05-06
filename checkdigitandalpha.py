x = raw_input()

digit = 0
alpha = 0

for i in x:
  if i.isdigit():
    digit+=1
    
    
  if i.isalpha():
    alpha+=1
    
    
if digit > 0 and alpha > 0:
  print "yes"
  
else:
  print "no"
