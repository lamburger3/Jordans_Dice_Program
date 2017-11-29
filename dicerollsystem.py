import random
import time

def roll_and_print(dice_amount, die_size, dice_modifer):
  #Initially, the sum of all the dice rolls is zero
  sum_of_dice_rolls = 0

  #Roll all the actual dice we ever need to roll
  for x in range(0, dice_amount):
    sum_of_dice_rolls = sum_of_dice_rolls + random.randint(1, die_size)
  
  #Add the dice modifier after we roll all the dice
  result_roll = sum_of_dice_rolls + dice_modifer

  #Tell the user the results of the dice roll
  print("Your true roll is: %d" % sum_of_dice_rolls)
  print("Your complete roll is: {0}".format(result_roll))

def main():
  try:
    amount = int(input("Enter the number of dice to roll: "))
    size = int(input("What is the size of this dice?: "))
    modifier = int(input("What is your modifier for this roll?: "))
    roll_and_print(amount, size, modifier)
  except:
    print("Please enter a valid number ty")
    return

while True:
  main()
