
Num  = int(input("Please Enter any Number: "))
f = Num
rev = 0.
while(Num > 0):
  
  Reminder = Num %10
  rev = (rev*10) + Reminder
  Num = Num // 10
c = int(rev)
if c == f:
  print "yes"
  
else:
  print "no"

  
