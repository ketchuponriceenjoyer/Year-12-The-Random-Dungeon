import time
import random

coins = 0
level = 1

health_max = 100
mana = 0


mana_regen_uses = 0
healing_uses =  0
buff_uses = 0

weapon1 = 0
weapon2 = 0

inventory = [{"coins": coins}, {"Healing items":"empty"}, {"buff items":"empty"}, {"Mana items":"empty"}]

weapon = [

  {"Name":"sword", "Attack":[  "heavy attack",random.randint(5,10),  "light attack",random.randint(1,4)  ]}, # 0
  {"Name":"shield", "Defense":[  "block",random.randint(3,10),  "parry",random.randint(1,100)  ] },# 1
  {"Name":"staff", "Magic":[  "fireball",random.randint(5,10),  "lightning Strike",random.randint(1,4)  ] }# 2
]

Healing_items = [
  {"Name":"empty", "Health_giver":"nothing"},
  {"Name":"Herbs", "Health_giver":random.randint(5,10)},
  {"Name":"health potion", "Health_giver":random.randint(18,25)},
  {"Name":"Big healing potion", "Health_giver":random.randint(28,36)},
  {"Name":"large healing potion", "Health_giver":50},
  {"Name":"Pie", "Health_giver":100},
]
if health_max >= 100:
  health = 100
  
Mana_items = [
  {"Name":"empty", "mana_giver":"nothing"},
  {"Name":"blueberry", "mana_giver":random.randint(5,10)},
  {"Name":"mana potion", "mana_giver":random.randint(18,25)},
  {"Name":"Big mana potion", "mana_giver":random.randint(28,36)},
  {"Name":"large mana potion", "mana_giver":50},
  {"Name":"Blueberry Pie", "mana_giver":100},
]
if mana >= 100:
  mana = 100

buff_items = [
  {"Name":"empty", "Attackboost":"nothing"},
  {"Name":"Magic Meat Rib", "Attackboost":random.randint(5,10)},
  {"Name":"strength potion", "Attackboost":random.randint(18,25)},
  {"Name":"Big strength potion", "Attackboost":random.randint(28,36)},
  {"Name":"large strength potion", "Attackboost":50},
  {"Name":"Chug Chug", "Attackboost":100},
]

inventory = [
  {"coins": coins}, 
  {"Healing items":Healing_items[0]}, 
  {"buff items":buff_items[0]}, 
  {"Mana items":Mana_items[0]}]



print("Welcome to the The Random Dungeon Game")
time.sleep(3.5)
print("In this game you wake up lost in a mysterious forest and is looking for a way out")
time.sleep(3.5)
print("you have a nothing in your inventory but see skeletal corpses on the ground")
time.sleep(3.5)
print("But on those corpses they appear to have a")
time.sleep(1.4)
print(weapon[0])
time.sleep(1.4)
print(weapon[1])
time.sleep(1.4)
print(weapon[2])
print("you can only pick 2 weapons")
time.sleep(3.5)
print("weapon choices", " 1 for sword", " 2 for shield", " 3 for staff")
time.sleep(2.5)


while True:
  try:
    Chosen_weapon_1 = int(input("Choose your first weapon -- "))
    if Chosen_weapon_1 == 1:
      weapon1 = weapon[0]

      coins = coins + random.randint(5, 10)
      inventory[1]["Healing items"] = Healing_items[1]
      healing_uses = healing_uses + random.randint(5, 10)
      inventory[2]["buff items"] = buff_items[1]
      buff_uses = buff_uses + random.randint(3, 5)
      
      break
    elif Chosen_weapon_1 == 2:
      weapon1 = weapon[1]

      coins = coins + random.randint(5, 10)
      inventory[1]["Healing items"] = Healing_items[1]
      healing_uses = healing_uses + random.randint(5, 11)
      
      break
    elif Chosen_weapon_1 == 3:
      weapon1 = weapon[2]

      coins = coins + random.randint(5, 10)
      inventory[1]["Mana items"] = Mana_items[1]
      mana_regen_uses = mana_regen_uses + random.randint(3, 11)
      inventory[3]["Mana items"] = Mana_items[1]
      
      break
  except ValueError:
    print("Not the number of the choices given")
    
    
time.sleep(1.5)
print("you chose", weapon1["Name"])

time.sleep(1.5)
print("weapon choices", " 1 for sword", " 2 for shield", " 3 for staff")


while True:
  try:
    Chosen_weapon_2 = int(input("Choose your second weapon -- "))
    if Chosen_weapon_2 == Chosen_weapon_1:
      print("you have already chosen this weapon, choose another weapon")
      continue
    elif Chosen_weapon_2 == 1:
      weapon2 = weapon[0]

      coins = coins + random.randint(5, 10)
      inventory[1]["Healing items"] = Healing_items[1]
      healing_uses = healing_uses + random.randint(5, 10)
      inventory[2]["buff items"] = buff_items[1]
      buff_uses = buff_uses + random.randint(3, 5)
      
      break
    elif Chosen_weapon_2 == 2:
      weapon2 = weapon[1]

      coins = coins + random.randint(5, 10)
      inventory[1]["Healing items"] = Healing_items[1]
      healing_uses = healing_uses + random.randint(5, 11)
      
      break
    elif Chosen_weapon_2 == 3:
      weapon2 = weapon[2]

      coins = coins + random.randint(5, 10)
      inventory[1]["Mana items"] = Mana_items[1]
      mana_regen_uses = mana_regen_uses + random.randint(3, 11)
      inventory[3]["Mana items"] = Mana_items[1]
      
      break
     
  except ValueError:
    print("Not the number of the choices given")
    
    
    
time.sleep(1.5)
print("you chose", weapon2["Name"])
time.sleep(3.5)
print("depending one what you chose, you also grab some items that will suit your build")
time.sleep(3.5)


print("--------------------------------------------------------")
print("First weapon - ", weapon1["Name"])
print("Second weapon - ", weapon2["Name"])
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                  INVENTORY                                                    ")
print("coins - ", inventory[0]["coins"])
print()
print("health items - ", inventory[1]["Healing items"]["Name"]," and regens", inventory[1]["Healing items"]["Health_giver"], " health with", healing_uses, "uses")
print("buff items - ", inventory[2]["buff items"]["Name"], "and boosts", inventory[2]["buff items"]["Attackboost"], "attack with", buff_uses, "uses")
print("mana items - ", inventory[3]["Mana items"]["Name"], "and regens mana by", inventory[3]["Mana items"]["mana_giver"], "mana with", mana_regen_uses, "uses")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("hello worl")
print("hello world")



