#Frame Diagram
#Mashrur Chowdhury
#Woodlands
#Creates a visual representation of portrait given width, height, frame width and matte width

#Checks if inputs are numbers
try:
  #Gets the inputs from the user
  WIDTH,LENGTH,MATTE,FRAME = [int(x) for x in input("(Portrait Width, Portrait Height, Matte Width, Frame Width): ").split(" ")]

#Creates Layers 1 to 2. Assembles the top frame, and the first matte line and multiplies by the frame and matte width respectively.
  layer1to2 = FRAME*(" "+"# "*(2*(FRAME+MATTE)+WIDTH)+ "\n") + \
            MATTE*(" "+"# "*FRAME + "+ "*(2*MATTE+WIDTH) + "# "*FRAME+"\n")

#Creates the middle layer. 
  mid = LENGTH*(" "+"# "*FRAME + "+ "*MATTE + "X "*WIDTH + "+ "*MATTE \
                 +"# "*FRAME+"\n")

#Assembles the portrait. Top Layer, then Middle Layer, then Top layer reversed.
  print(layer1to2+mid[:len(mid)-1]+layer1to2[::-1])

#If inputs are letters, gives error message.
except ValueError:print("That's not the right format. You might have a space at the end or a letter in it")