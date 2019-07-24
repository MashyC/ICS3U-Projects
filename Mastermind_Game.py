from random import randint
t=""

for i in range (0,8):
  t+=str(randint(0,9))

def play(tries):
  print(" ")
  guess = input("Guess:")

  if guess == "hint":
    print(t)
    exit()
  def rightPos(t,guess,v):
    for i in range(len(guess)):
      if guess[i] == t[i]:
        v+=1
    return(v)
    
  if rightPos(t,guess,0) == len(t):
    print("You guessed the code in ", tries+1, "tries!")
    exit()
  print("Correct Position:",rightPos(t,guess,0))

  def rightGuess(t,guess,v):
    for i in range(len(guess)):
      if guess[i] in t:
        v+=1
    return(v)

  print("Correct Guess:", rightGuess(t,guess,0))

  tries+=1
  play(tries)

play(0)
