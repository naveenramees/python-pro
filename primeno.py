givnum = int(input("Enter the number:"))

if givnum > 1:
  
   for i in range(2,givnum):
       if (givnum % i) == 0:
           print "No"
       
           break
   else:
       print "yes"
  
