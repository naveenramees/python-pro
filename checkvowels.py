n = raw_input()
digit = 0
for i in n:
  if i in "aeiou":
    digit+=1
    

if digit == 0:
  print "no"
  
if digit != 0:
  print "yes"
