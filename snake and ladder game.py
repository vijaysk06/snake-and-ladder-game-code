import random
print("Welcome to my Game of Snakes and Ladders")
print()

import cv2
grey_image = cv2.imread('Board_snake and ladder.jpg',0)
cv2.imshow('graysale image',grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('grayscale.jpg',grey_image)

pos=0
def game(pos):
  print("Press 'R' to roll\n'M' to main menu")
  inp=input(">>")
  while(inp!='M' or inp!='m'):
    dice=random.randint(1,6)
    print("You rolled",dice)
    if(dice==1):
      pos+=1
    if(dice==2):
      pos+=2
    if(dice==3):
      pos+=3
    if(dice==4):
      pos+=4
    if(dice==5):
      pos+=5
    if(dice==6):
      pos+=6
    if(pos==1):
      pos=38
      print("Hooray! Ladder")
    if(pos==4):
      pos=14
      print("Hooray! Ladder")
    if(pos==8):
      pos=30
      print("Hooray! Ladder")
    if(pos==21):
      pos=42
      print("Hooray! Ladder")
    if(pos==28):
      pos=76
      print("Hooray! Ladder")
    if(pos==32):
      pos=10
      print("Ouch...SnakeBite!")
    if(pos==36):
      pos=6
      print("Ouch...SnakeBite!")
    if(pos==48):
      pos=26
      print("Ouch...SnakeBite!")
    if(pos==50):
      pos=67
      print("Hooray! Ladder")
    if(pos==62):
      pos=18
      print("Ouch...SnakeBite!")
    if(pos==71):
      pos=92
      print("Hooray! Ladder")
    if(pos==80):
      pos=99
      print("Hooray! Ladder")
    if(pos==88):
      pos=24
      print("Ouch...SnakeBite!")
    if(pos==95):
      pos=56
      print("Ouch...SnakeBite!")
    if(pos==97):
      pos=78
      print("Ouch...SnakeBite!")
    if(pos==100):
      print("You have Won!!")
      print("Winner Winner, Chicken Dinner")
      break
    if(pos<100):
      print("You are currently at ",pos)
    if(pos>100):
      print("Roll again, It's impossible to move like that")
      pos=pos-dice
      print("You are currently at ",pos)
    inp=input(">>")
  

print("Press 'S' to start the game\nPress'E' to Exit")
input1=input(">>")

if(input1=='S' or input1=='s'):
  game(pos)