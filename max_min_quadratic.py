"""
Min/Max on an Interval
Mashrur Chowdhury
Woodlands
Calculates the occurance of maximum and minimum values on a quadratic formula.
"""

a,b,c=[int(x) for x in input("Coefficients of equation (Ex: '4 5 6'): ").split(" ")]
start=float(input("Starting x value: "))
end=float(input("Ending x value: "))
step=float(input("Step Interval: "))

coord_x =[]
coord_y =[]
x=start

while x<=end+0.5*step:
  y = a*x**2+b*x+c
  coord_x.append(x)
  coord_y.append(y)
  x+=step

max_x = round(coord_x[coord_y.index(max(coord_y))],2)
min_x = round(coord_x[coord_y.index(min(coord_y))],2)

print("Maxiumum when x =", max_x, "(f("+str(max_x)+") =", str(round(max(coord_y),2))+")")
print("Miniumum when x =", min_x, "(f("+str(min_x)+") =", str(round(min(coord_y),2))+")")
