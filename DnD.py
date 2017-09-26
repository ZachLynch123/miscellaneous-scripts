
# Description	: This will randomly select two numbers, like throwing dice.

import random
class Die(object):
  #A dice has a feature of number about how many sides it has when it's established,like 6.
  def __init__(self):
    self.sides=6
    
  """because a dice contains at least 4 planes.
  So use this method to give it a judgement when you need to change the instance attributes."""
  def set_sides(self, sides_change):
    if sides_change>=4:
      if sides_change != 6:
        self.sides = sides_change
    else:
      print("wrong sides! sides set to 6")
      
  def roll(self):
    return random.randint(1, self.sides)

num_of_dice = input("How many dice?: " )

sides_of_dice = input("Rolling a D")

i = 0

for i in range (num_of_dice):
  d = Die()
  d1 = Die()
  d.set_sides(sides_of_dice)
  print (d.roll())
