adult = 0;child = 0 ;senior = 0
def program(adult,child,senior):
  x = input('Do you want to buy a ticket? [Y/N] ')
  if x[0].lower() == "n":
    subtotal = int(adult)*12 + int(child)*8 + int(senior)*6
    salestax = int(subtotal)*0.13
    total = int(subtotal) + int(salestax)
    print ("You purchased:",adult,"adult tickets",child,"child tickets and" ,senior,"senior tickets")
    print ("Subtotal: $",round(subtotal,2))
    print ("Sales Tax: $",round(salestax,2))
    print ("Total: $",round(total,2))
    exit()
  
  if x[0].lower() == "y":
    print ('The ticket prices are: \n $12 per adult ticket, \n $8 per child, and \n $6 for seniors. \n ')
    ticket = input('Do you want to purchase an adult, child or senior ticket? ')
    
    if ticket[0].lower() == "a":
      adult+=1
      print ("You have purchased an adult ticket")
      program(adult,child,senior)
           
    elif ticket[0].lower() == "c":
      child+=1
      print ("You have purchased a child ticket")
      program(adult,child,senior)

    else:
      senior+=1
      print ("You have purchased a senior ticket")
      program(adult,child,senior)

program(adult,child,senior)