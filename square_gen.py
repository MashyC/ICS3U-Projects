#Assembles the square using both types of lines if applicable
def drawSquare(size,hollow,char):
  if hollow:
    line = (char+" ")*size+"\n"; 
    line2 = char+" "+" "*(size*2-4)+char+"\n"
    print(line+line2*(size-2)+line)
  else:
    line = (char+" ")*size+"\n"
    print(size*line)
    
#Asks for the size, if hollow, and type of the square and sends to drawSquare.
def start():
  r=0
  while r==0:
    try:
      size=abs(int(input("What is the size of the square: ")))
      r+=1
    except ValueError:
      print("That is not a number!")
  if r==1:
    hollow=(input("Is the square hollow? (Y or N): "))
    if hollow.upper()=="Y":
      hollow=True
      char=(input("What character is the square made out of: "))
      drawSquare(size,hollow,char)
    elif hollow.upper()=="N": 
      hollow=False
      char=(input("What character is the square made out of: "))
      drawSquare(size,hollow,char)
    else:
      print("That is not a valid choice!")
      start()

start()