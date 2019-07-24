#Mashrur Chowdhury
#Woodlands
#Quadratic Calculator

#importing square root module for discriminant
from math import sqrt
print("--QUADRATIC CALCULATOR--")

#prints the number of roots
def numRoots(a,b,c,d):
  if d>0:print("There are two roots.")
  elif d==0:print("There is one root.")
  else:print("There are no roots of this equation.")
  main(a,b,c)

#prints the coordinates of the roots if there are any.
def coordsRoot(a,b,c,d):
  if d<0:
    print("There are no roots for this equation.")
    main(a,b,c)
  elif d>0:
    x1=round((-b+sqrt(d))/(2*a),2)
    x2=round((-b-sqrt(d))/(2*a),2)
    print("X1: ("+str(x1)+", 0)")
    print("X2: ("+str(x2)+", 0)")
    main(a,b,c)
  else:
    x1=round((-b+sqrt(d))/(2*a),2)
    print("X1: ("+str(x1)+", 0)")

#Determines the coordinate of the vertex
def vertex(a,b,c):
  x=round(-b/(2*a),2)
  y=round(a*x**2+b*x+c,2)
  print("Vertex: ("+str(x)+",",str(y)+")")
  main(a,b,c)

#Finds the maximum or minimum value of the equation.
def maxmin(a,b,c):
  x=-b/(2*a)
  y=a*x**2+b*x+c
  if a<0:print("Maximum: y =",y)
  else:print("Minimum: y =",y)
  main(a,b,c)

#Lists all available functions
def main(a,b,c):
  d=b**2-(4*a*c)
  print("\n--AVAILABLE FUNCTIONS--\n1. # Of Roots\n2. Coordinate of Root\n3. Location of Vertex\n4. Min/Max\n5. Exit")
  choice=int(input("\nWhich function would you like to do (1,2,3,4,5): "))

  if choice==1:numRoots(a,b,c,d)
  elif choice==2:coordsRoot(a,b,c,d)  
  elif choice==3:vertex(a,b,c) 
  elif choice==4:maxmin(a,b,c)
  elif choice==5:print("Bye!");exit()
  else:print("That is not a valid choice!");main(a,b,c)    

#getting the coefficients from the user
def get():
  try:
    a=float(input("A: "));b=float(input("B: "));c=float(input("C: "))
    if a == 0:
      print("The A Value must not be Zero!")
      get()
    main(a,b,c)
  except ValueError: print("That's not a number!")
get()
