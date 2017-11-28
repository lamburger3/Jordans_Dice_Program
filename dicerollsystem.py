import random
import time

def roll():
  mod = input("What is your modifier for this roll?: ")
  random_roll = (random.randint(1,20))
  sum = int(mod) + int(random_roll)
  print("Your true roll is:")
  time.sleep(0.5)
  print(random_roll)
  time.sleep(1)
  print("Your complete roll is:")
  time.sleep(0.5)
  print(sum)

  roll()

roll()
