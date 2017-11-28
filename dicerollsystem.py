import random
import time

def roll_and_print(die_size, dice_modifer):
  random_roll = random.randint(1, die_size)
  result_roll = random_roll + dice_modifer
  print("Your true roll is: %d" % random_roll)
  print("Your complete roll is: {0}".format(result_roll))

def main():
  try:
    size = int(input("What is the size of this dice?: "))
    modifier = int(input("What is your modifier for this roll?: "))
    roll_and_print(size, modifier)
  except:
    print("Please enter a valid number ty")
    return

while True:
  main()
