import art
import random
from replit import clear



game_on=True
while game_on:
  entry = input("do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no ").lower()
  clear()
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  if entry=='y':
    print(art.logo)
    your_hand=[]
    computer_hand=[]
    score=0
    com_score=0
    for i in range(2):
      x=random.choice(cards)
      your_hand.append(x)
      score+=x
    y=random.choice(cards)
    computer_hand.append(y)
    print(f"Your Cards: {your_hand} , current score {score}")
    print(f"Computer's first card {computer_hand}")
    com_score+=y
    if score==21:
      print("    Blackjack!!,You have won")
      print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
      print(f"Computer's final hand {computer_hand},final score {com_score}")
      break
   
    while 2>1:
      cont=input("Type 'y' to get another card and type 'n' to pass ")
      if score==21:
        print("    Blackjack!!,You have won")
        print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
        print(f"Computer's final hand {computer_hand},final score {com_score}")
        break
      if cont == 'y':
        x=random.choice(cards)
        your_hand.append(x)
        score+=x
        print(f"Your Cards: {your_hand} , current score {score}")
        print(f"Computer's first card {computer_hand}")
        if score==21:
          print("    Blackjack!!,You have won")
          print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
          print(f"Computer's final hand {computer_hand},final score {com_score}")
          break
        if score>21 and 11 in your_hand:
          your_hand.remove(11)
          your_hand.append(1)
          score=score-10
          print(f"Your Cards: {your_hand} , current score {score}")
          print(f"Computer's first card {computer_hand}")
        if score>21:
          # your_hand.remove(11)
          # your_hand.append(1)
          y=random.choice(cards)
          computer_hand.append(y)
          com_score+=y
          print("    You Went Over.You Lose")
          print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
          print(f"Computer's final hand {computer_hand},final score {com_score}")
          break
        
          
      elif cont=='n':
        if score<17:
          print("You can't pass this round the dealer gives you a new card")
          x=random.choice(cards)
          your_hand.append(x)
          score+=x
        
        
        y=random.choice(cards)
        computer_hand.append(y)
        com_score+=y
        while com_score<17:
          y=random.choice(cards)
          computer_hand.append(y)
          com_score+=y
        if com_score>21 and 11 in computer_hand:
          computer_hand.remove(11)
          computer_hand.append(1)
          com_score=com_score-10
        if com_score>21 or 21-score<21-com_score:
          print("    Voila!!You Win ")
          print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
          print(f"Computer's final hand {computer_hand},final score {com_score}")
          break
        elif 21-com_score<21-score:
          print("    You Lose :( Better Luck Next Time")
          print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
          print(f"Computer's final hand {computer_hand},final score {com_score}")
          break
        elif com_score==score:
          print("    It's a draw")
          print(f"Your Final Hand: {your_hand} , Your Final Score {score}")
          print(f"Computer's final hand {computer_hand},final score {com_score}")
        break
        
        
   
      
      
  elif entry =='n':
    game_on=False
    
