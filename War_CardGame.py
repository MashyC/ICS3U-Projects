from random import randint
from time import sleep

cards = [ ["A❤", "A◆", "A♣", "A♠"],
          ["2❤", "2◆", "2♣", "2♠"],
          ["3❤", "3◆", "3♣", "3♠"],
          ["4❤", "4◆", "4♣", "4♠"],
          ["5❤", "5◆", "5♣", "5♠"],
          ["6❤", "6◆", "6♣", "6♠"],
          ["7❤", "7◆", "7♣", "7♠"],
          ["8❤", "8◆", "8♣", "8♠"],
          ["9❤", "9◆", "9♣", "9♠"],
          ["10❤", "10◆", "10♣", "10♠"],
          ["J❤", "J◆", "J♣", "J♠"],
          ["Q❤", "Q◆", "Q♣", "Q♠"],
          ["K❤", "K◆", "K♣", "K♠"] ]

comp = []
user = []

for i in range(26):
  for y in range(0,len(cards)-1):
    if len(cards[y]) == 0:
      del cards[y]
  a = randint(0, len(cards)-1)
  b = randint(0, len(cards[a])-1)
  comp.append(cards[a][b])
  del cards[a][b]

for i in range(26):
  for y in range(0,len(cards)-1):
    if len(cards[y]) == 0:
      del cards[y]
  a = randint(0, len(cards)-1)
  b = randint(0, len(cards[a])-1)
  user.append(cards[a][b])
  del cards[a][b]

print(user)
print(comp)
e=0
def game(e):
  sleep(0.005)
  if len(comp) == 52:
    print("COMPUTER WIN")
    exit()
  elif len(user) == 52:
    print("YOU WIN")
    exit()
  print("")

  n_1 = randint(0,len(user)-1)
  n_2 = randint(0,len(comp)-1)
  u = list(user[n_1])
  c = list(comp[n_2])
  print("You: " + "".join(u) + "               Cards:" + str(len(user)))
  print("Computer: " + "".join(c) + "          Cards:" + str(len(comp)))
  print("Turn: ", e)
  
  if u[0] == "J":
    u[0] = 11
  if u[0] == "Q":
    u[0] = 12
  if u[0] == "K":
    u[0] = 13
  if u[0] == "A":
    u[0] = 14


  if c[0] == "J":
    c[0] = 11
  if c[0] == "Q":
    c[0] = 12
  if c[0] == "K":
    c[0] = 13
  if c[0] == "A":
    c[0] = 14

  u = int(u[0])
  c = int(c[0])

  if u>c:
    print("")
    print("You win!")
    print("")
    user.append(comp[n_2])
    del comp[n_2]
    e+=1
    game(e)
  elif u<c:
    print("")
    print("Computer wins!")
    print("")
    comp.append(user[n_1])
    del user[n_1]
    e+=1
    game(e)
  else: 
    print("")
    print("WARRRRRRR!")
    print("")
    game(e)

game(e)
