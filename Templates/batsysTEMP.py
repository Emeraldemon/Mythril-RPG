#Import stuff
import random
from wep_index import swordskillset
from wep_index import shieldskillset
from wep_index import spellbskillset

#Boss stats
DamageED = 0
healthED = 100
BattleED = 1
#Playerstats

Damage = 0
attk = 100
dfns = 100
coins = 500
health = 1000
c = 1

#strings
commencement1 = ""
intro1 = ""
supermove1 = ""
bossname1 = ""
smallermove1 = ""
victorymsg1 = ""

eldmsg = "" #When you get your turn

print(commencement)
import random
while c > 0:
  if random.random() < 0.5:
      from batmechs import eldrichfight
      eldrichfight(intro1, supermove1,health,healthED,bossname1,smallermove1)
  else:
      print("=*=*=*=*=*=*=*=*")
      if healED <= 0:
        print(victorymsg)
        print("Y O U    W O N")
        break
      print(eldmsg)
      #PLAYER
      print("(1)Dodge")
      print("(2)Retreat")
      print("(3)Equipment skill")
            mve = int(input())
      if mve == 3:
              print("Equipment used")
              wepset = 4
              if wepset == 1:
                swordskillset(healthED)
              elif wepset == 2:
                shieldskillset(healthED)
              elif wepset == 4:
                spellbskillset(healthED)
      elif mve == 2:
          print("GAME OVER")
          print("A spell was cast such as to make your fear the very poison for your demise")
          break
      elif mve == 1:
          print("You dodged the attack")
          if random.random() < 0.4:
            print("Eldrich used Mindread!")
            health -= 10
  print("Player HP: ", health)
  print("Eldrich HP: ", healthED)
      
      

        
      
