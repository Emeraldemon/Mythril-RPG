#let's say we define a variable 'coins' to be 500
def shop(money,charge,dodge,bag):
  #Will have 4 items for now
  print("Type the integer of whichever item you wish to buy")
  print("(1) Sword ~ 300")
  print("(2) Shield ~ 200")
  print("(3) Armour ~ 400")
  print("(4) Spell-book ~ 100")
  itm = int(input())
  if itm == 1:
    bag = 1
    money -= 300
    print("Thanks for buying!")
  elif itm == 2:
    bag = 2
    money -= 200
    print("Thanks for buying!")
  elif itm == 3:
    bag = 3
    money -= 400
    print("Thanks for buying!")
  elif itm == 4:
    money -= 100
    bag = 4
    print("Thanks for buying!")

  if money < 0:
    print("You don't have enough coins for that")
  print("Remaining coins: ", money)
