box = int(input("Enter the num:"))

if (box % 4) == 0:
   if (box % 100) == 0:
       if (box % 400) == 0:
           print "yes"
       else:
        print "No"
   else:
    print "yes"
else:
  print "No"
  
