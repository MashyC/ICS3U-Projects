#6 lines ;)

from random import randint; score=0
for i in range(50):
  if score==5:print("you win, but like not really!");exit()
  n1=randint(0,20);n2=randint(0,20);add=str(n1)+"+"+str(n2)+": ";a=int(input(add))
  if a==n1+n2:score+=1;print("score: ",score)
  else:score-=1