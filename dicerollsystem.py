import random
import time
mod = input("What is your modifier for this roll?: ")


roll = (random.randint(1,20))
sum = int(mod) + int(roll)
print ("Your true roll is:")
time.sleep(0.5)
print (roll)
time.sleep(2)
print ("Your complete roll is:")
time.sleep(0.5)
print (sum)
time.sleep(3)

roll()
