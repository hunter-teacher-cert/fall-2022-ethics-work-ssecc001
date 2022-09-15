import random

def Nim():
  stones = 12
  while stones > 0:
    stonesTaken = input("Please enter a number from 1-3 ")
    stonesTaken = int(stonesTaken)
    stones = stones - stonesTaken
  
    print("There are " + str(stones) + " left")

    if(stones <= 0):
      print("You win!")
        
    print("Computers Turn")
    stonesTaken = random.randint(1,3)
    stones = stones - stonesTaken
    print("The Computer took " + str(stonesTaken))
    print("There are " + str(stones) + " left")

    if(stones <= 0 ):
      print("Computer wins!")

Nim()
