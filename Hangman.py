import sys

word = input("Enter Word:")
players = input("How many players?")
print("")
player_list = []

lives = 5

for n in range(1,int(players)+1):
  name = input("Player " + str(n) + " write your name:")
  player_list.append(name) 

t=""
for i in word:
  t+="_ "
print(t)
print("")

live = 5
n=0
yes=-1
guesses = [] 

def check(player_list, live,n, yes,guesses):
  v = ""
  for gu in guesses:
    print(gu)
    if gu in word:
        yes=yes+1
        print("Thats in the word!")
        for i in word:
          if i == gu:
            v=v+gu+" "
          else:
            v=v+"_ "
        n=n+1
        play(player_list, live,n,yes,guesses)
    else:
        print("Uh-oh! That letter isn't in the word!")
        live = live-1
        print("Lives: ", live)
        print("")
        if live==0:
          print("Oh no! You've ran out of lives. :(")
          sys.exit()
        n=n+1
        play(player_list, live,n,yes,guesses)
  print(v)
  
def play(player_list, live,n,yes,guesses):
    if n>len(player_list)-1:
      n=n-len(player_list)
      print("")
      guess1 = input("Take a guess, " + player_list[n] + ":")
      guesses.append(guess1)
      check(player_list, live,n,yes,guesses)
    else:
      print("")
      guess1 = input("Take a guess, " + player_list[n] + ":")
      guesses.append(guess1)
      check(player_list, live,n,yes,guesses)

play(player_list, live,n,yes,guesses)


