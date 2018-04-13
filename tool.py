tool = int(input("Enter the tool:"))
if (tool % 4) == 0:
   if (tool % 100) == 0:
       if (tool % 400) == 0:
           print "yes"
       else:
        print "No"
   else:
    print "yes"
else:
  print "No"
  
