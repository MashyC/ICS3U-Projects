#Mashrur Chowdhury
#Woodlands Computer Science
#Inventory Management System (TextFiles)

import os
#Creating the inventory and price variables
inv = {};total=0;bill=[]

#Reads andd checks if anything is already in the textfile and stores it into the temporary inventory
inv1 = open("inventory.txt", "r")
x=0
num_lines = sum(1 for line in open('inventory.txt'))
while x!=num_lines:
    line=inv1.readline()
    if "[" in line:
        line.rstrip("\n")
        price=inv1.readline().rstrip("\n")[1:]
        stock = inv1.readline().rstrip("\n")
        inv[line.rstrip("\n")[1:-1].capitalize()] = [price, int(stock)]
    x+=1
#closes the textfile
inv1.close()

print("--MINI-WALMART INVENTORY--")

#Function for adding an item
def add_item(inv, total, bill):
  r=0
  while r==0:
    try:
      item=input("\nWhat item do you want to add: ").capitalize()
      if item in inv:
        print("That item is already added!")
        manage(total,bill)
      price=abs(float(input("\nWhat is the price of "+item+" (No Dollar Sign): ")))
      price=format(price,".2f")
      stock=int(input("\nHow many "+item+" are there (Number only): "))
      inv[item]=[price,stock]
      r+=1
      manage(total,bill)
    except ValueError:
      print("That is not an integer!")

#Function for removing an item
def remove_item(inv, total, bill):
  item=input("\nWhat item do you want to remove: ").capitalize()
  if item not in inv:
    print("That item doesn't exist in our system!")
    manage(total,bill)
  inv.pop(item)
  print(item,"has been removed.")
  manage(total,bill)

#Function for listing all items
def list_item(inv,total,bill):
  print("--INVENTORY--")
  for i in inv:print("   "+i)
  manage(total,bill)

#Function for displaying all details of an item.
def inquire(inv,total,bill):
  item=input("\nWhich item are you inquiring about: ").capitalize()
  if item not in inv:
    print("That item does not exist in our system.")
    manage(total,bill)
  print("\n---"+item.upper()+"---")
  print("Unit Price: $"+str(inv[item][0]))
  print("# in stock:",inv[item][1])
  manage(total,bill)

#Function for purchasing an item
def purchase(inv,total,bill):
  item=input("\nWhich item are you purchasing: ").capitalize()
  if item not in inv:
    print("That item does not exist in our system.")
    manage(total,bill)
  r=0
  while r==0:
    try:
      num=abs(int(input("How many "+item+" are you purchasing: ")))
      r+=1
    except ValueError:
      print("Thats not a number.")
  if inv[item][1]==0:
    print("That item is not in stock right now, sorry!")
  elif num>inv[item][1]:
    print("You have purchased", inv[item][1], item, "for $",format(float(inv[item][0])*inv[item][1],".2f"))
    print("\nWe only have", inv[item][1],"in stock right now.", inv[item][1],"will be delivered today and the remaining", num-inv[item][1],"will be delivered tomorrow.")
    total+=float(inv[item][0])*inv[item][1]
    bill.append([item.capitalize(), inv[item][1], float(inv[item][0])*inv[item][1]])
    inv[item][1]=0
  else:
    print("You have purchased", num, item, "for $"+format(float(inv[item][0])*num,".2f"))
    total+=float(inv[item][0])*num
    bill.append([item.capitalize(), num, float(inv[item][0])*num])
    inv[item][1]-=num
  manage(total,bill) 

#Function for updating an items price or stock
def update(inv,total,bill):
  item=input("\nWhich item are you updating: ").capitalize()
  if item not in inv:
    print("That item does not exist in our system.")
    manage(total,bill)
  r=0
  while r==0:
    try:
      n_price=float(input("What is the new price of "+item+": "))
      n_price=format(n_price,".2f")
      n_stock=int(input("What is the new stock of "+item+": "))
      r+=1
    except ValueError:
      print("That is not a number!")
  inv[item][0]=n_price

  inv[item][1]=n_stock
  manage(total,bill)

#Function for final bill
def escape(inv,total,bill):
  #Removes the preexisting inventory file to make a new one
  os.remove("inventory.txt")
  for key, value in inv.items():
      #Formarts each item, price and stock number
      name = "["+key.upper()+"]\n"
      price= "$"+str(value[0])+"\n"
      stock = str(value[1])+"\n\n"
      with open("inventory.txt", "a+") as inventory:
          #Adds each item and info to textfile
          inventory.write(name)
          inventory.write(price)
          inventory.write(stock)
  if total==0:
    print("\nThank you. Have a nice day!")
  else:
    print("\n--FINAL BILL--")
    for i in bill:
      print(str(i[1])+"x",i[0]+": $"+format(i[2],".2f"))
    gst=round(total*0.13,2)
    print("SUBTOTAL: $"+format(total,'.2f'))
    print("GST: $"+format(gst,'.2f'))
    print("TOTAL: $"+format(total+gst,'.2f'))
    print("\nThank you. Have a nice day!")
    quit()

#Starter function to ask usEr for which operation they want to do.
def manage(total,bill):
  x=input("\nAdd, Remove, List, Inquire, Purchase, Update, or Exit: ")[0].lower()
  if x=="a":add_item(inv, total, bill)
  elif x=="r":remove_item(inv,total,bill)
  elif x=="l":list_item(inv,total,bill)
  elif x=="i":inquire(inv,total,bill)
  elif x=="p":purchase(inv,total,bill)
  elif x=="u":update(inv,total,bill)
  elif x=="e":escape(inv,total,bill)
  else:
    print("Thats not a valid input!")
    manage(total,bill)
manage(total,bill) 
