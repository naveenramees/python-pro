ye = int(input("Enter the value:"))
if (ye % 4) == 0:
   if (ye % 100) == 0:
       if (ye % 400) == 0:
           print "yes"
       else:
        print "No"
   else:
    print "yes"
else:
  print "No"
  
