from art import logo
#from replit import clear
import random

wanna_play = True

Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while wanna_play ==True:
  play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
  
  your_list=[]
  Computer_list=[]
  your_total = 0
  Computer_total =0
  
  if play =='y':
    #clear()
    print(logo)

    
    your_list.append(random.choice(Cards))
    your_list.append(random.choice(Cards))

    Computer_list.append(random.choice(Cards))
    Computer_list.append(random.choice(Cards))

    print(f'Your     cards are : {your_list}')
    print(f'Computer first card is : [{Computer_list[0]}]\n')

    new_card_choice = input("Do you want new card? Type 'y' or 'n': ")

    if new_card_choice == 'y':
      your_list.append(random.choice(Cards))
      print(f'\nYour cards are   : {your_list}')
      print(f'Computer cards are : {Computer_list}\n')

    for ele in range(0, len(your_list)):
      your_total = your_total + your_list[ele]

    
    
    if your_total > 21:
      
      print(f"your total is more then 21 : {your_total}")
      print("Computer Wins")

    else:
      for ele in range(0, len(Computer_list)):
        Computer_total = Computer_total + Computer_list[ele]

      print(f"your     cards total is : {your_total}")
      print(f"Computer cards total is : {Computer_total}\n")
        
      if your_total > Computer_total:
        print("You Wins")

      elif your_total == Computer_total:
        print("Draw")
          
      else:
        print("Computer Wins")

  else:
    print("ok bye")
    wanna_play = False
  

  
  