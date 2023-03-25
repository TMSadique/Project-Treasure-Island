print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

decision1 = input("\nYou are at cross-road, where do you want to go? type 'left' or 'right'. \n").lower()

if decision1 == "left":
  decision2 = input("\nYou have reached a lake, there is an island in the middle of the lake. Type if you\'d 'swim' or 'wait' for the boat?\n").lower()

  if decision2 == "wait":
    decision3 = input("\nYou have cossed the lake and arrived at the island unharmed. There is a house with 'red', 'blue' and 'yellow' doors. Which colour door would you choose?\n").lower()
    
    if decision3 == "red":
      print(f"It's room full of fire. GAME OVER!")
    elif decision3 == "blue":
      print(f"Its's room full of beasts. GAME OVER!")      
    elif decision3 == "yellow":
      print(f"\n\nThe room is full of treasure. YOU WIN!")
      print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`  
      ''')
    
    else:
      print("You chose a door that doesn't exists. GAME OVER!")
  
  else:
    print(f"You were attacked by trout. GAME OVER!")
  
else:
  print(f"You fell into a hole, GAME OVER!")
