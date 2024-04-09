import time
import random

weapon = [

  {"name":"sword", "attack":[  "heavy attack",random.randint(5,10),  "light attack",random.randint(10,15)  ]}, # 0
  {"name":"whip", "attack":[  "strike",random.randint(3,10),  "rip",random.randint(1,6)  ] },# 1
  {"name":"staff", "attack":[  "fireball",random.randint(5,10),  "lightning Strike",random.randint(1,4)  ] },# 2
  {"name":"bow", "attack":[  "light arrow",random.randint(5,10),  "piercing arrow",random.randint(1,4)  ] }# 2
]

Healing_items = [
  {"name":None, "health_giver":None},
  {"name":"herbs", "health_giver":random.randint(5,10)},
  {"name":"health_potion", "health_giver":random.randint(18,25)},
  {"name":"big_healing_potion", "health_giver":random.randint(28,36)},
  {"name":"large_healing_potion", "health_giver":50},
  {"name":"pie", "health_giver":100},
]

  
Mana_items = [
  {"name":None, "mana_giver":None},
  {"name":"blueberry", "mana_giver":random.randint(5,10)},
  {"name":"mana_potion", "mana_giver":random.randint(18,25)},
  {"name":"big_mana_potion", "mana_giver":random.randint(28,36)},
  {"name":"large_mana_potion", "mana_giver":50},
  {"name":"blueberry_Pie", "mana_giver":100},
]

buff_items = [
  {"name":None, "attack_boost":"nothing"},
  {"name":"Magic_Meat_Rib", "attack_boost":random.randint(5,10)},
  {"name":"strength_potion", "attack_boost":random.randint(18,25)},
  {"name":"Big_strength_potion", "attack_boost":random.randint(28,36)},
  {"name":"large_strength_potion", "attack_boost":50},
  {"name":"Chug_Chug", "attack_boost":100},
]


Enemy_Mob = [
  {"name":"nobody", "attack":"nothing"},
  {"name":"goblin", "health":random.randint(5, 10), "attack":["jab",random.randint(5,10), "roundhouse",random.randint(10,20)]},
  {"name":"orc", "health":random.randint(10, 20), "attack":["boulder throw",random.randint(8,15), "shoulder strike",random.randint(24,30)]},
  {"name":"giant", "health":random.randint(20, 30), "attack":["smash",random.randint(15,20), "stomp",random.randint(30,40)]},
  
  ]
Healing_slots = [None, None, None]
Healing_uses = [0,0,0]

Buff_items_slots = [None, None, None]
Buff_items_uses = [0,0,0]

Mana_items_slots = [None, None, None]
Mana_uses = [0,0,0]

coins = 0

Player_status_inventory = [
  {"health": 100, "mana": 50},#0
  {"coins": coins},#1
  {"weapon_1": None, "weapon_2": None}, #2
  {"healing_items":Healing_slots, "healing_uses":Healing_uses},#3
  {"buff_items":Buff_items_slots, "buff_uses":Buff_items_uses},#4
  {"mana_items":Mana_items_slots, "mana_uses":Mana_uses},#5
]

global healing_uses 
  
print("Welcome to the The Random Dungeon Game")
  #time.sleep(3.5)
print("In this game you wake up lost in a mysterious forest and is looking for a way out")
  #time.sleep(3.5)
print("you have a nothing in your inventory but see skeletal corpses on the ground")
  #time.sleep(3.5)
print("But on those corpses they appear to have a")
  #time.sleep(1.4)
print(weapon[0])
  #time.sleep(1.4)
print(weapon[1])
  #time.sleep(1.4)
print(weapon[2])
print("you can only pick 2 weapons")
  #time.sleep(3.5)
print("weapon choices", " 1 for sword", " 2 for shield", " 3 for staff")
  #time.sleep(2.5)
  
  
while True:
  try:
    Chosen_weapon_1 = int(input("Choose your first weapon -- "))
      #chosen sword for weapon1
    if Chosen_weapon_1 == 1:
      Player_status_inventory[2]["weapon_2"] = weapon[0]
      
      Healing_slots[0] = Healing_items[1]["name"]
      Healing_uses[0] = random.randint(1,5)
      
      coins + random.randint(1,10)
      
      Buff_items_slots[0] = buff_items[1]["name"]
      Buff_items_uses[0] = random.randint(1,5)
      break
        
    elif Chosen_weapon_1 == 2:
        #chosen whip for weapon1
      Player_status_inventory[2]["weapon_2"] = weapon[1]
      
      Healing_slots[0] = Healing_items[1]["name"]
      Healing_uses[0] = random.randint(1,5)
      coins + random.randint(1,10)
      break
        
    elif Chosen_weapon_1 == 3:
      #chosen staff for weapon1
      coins + random.randint(1,10)
      
      Player_status_inventory[2]["weapon_2"] = weapon[2]
      
      Healing_slots[0] = Healing_items[1]["name"]
      Healing_uses[0] = random.randint(1,5)
      
      Mana_items_slots[0] = Mana_items[1]["name"]
      Mana_uses[0] = random.randint(1,5)
      break
  except ValueError:
    print("not in choices")
  
    
while True:
  try:
    Chosen_weapon_2 = int(input("Choose your Second weapon -- "))
    #chosen sword for weapon1
    if Chosen_weapon_2 == 1:
      Player_status_inventory[2]["weapon_1"] = weapon[0]
      
      Healing_slots[1] = Healing_items[1]["name"]
      Healing_uses[1] = random.randint(1,5)
      
      coins + random.randint(1,10)
      
      Buff_items_slots[1] = buff_items[1]["name"]
      Buff_items_uses[1] = random.randint(1,5)
      break
    elif Chosen_weapon_2 == 2:
      #chosen whip for weapon1
      Player_status_inventory[2]["weapon_1"] = weapon[1]
        
      Healing_slots[1] = Healing_items[1]["name"]
      Healing_uses[1] = random.randint(1,5)
      
      coins + random.randint(1,10)
      break
    elif Chosen_weapon_2 == 3:
      #chosen staff for weapon1
      coins + random.randint(1,10)
      
      Player_status_inventory[2]["weapon_1"] = weapon[2]
      
      Healing_slots[1] = Healing_items[1]["name"]
      Healing_uses[1] = random.randint(1,5)
      
      Mana_items_slots[1] = Mana_items[1]["name"]
      Mana_uses[1] = random.randint(1,5)
      
      break
    elif Chosen_weapon_2 == Chosen_weapon_1:
      print("You can't have the same weapon twice")
      continue
        
  except ValueError:
    print("not in choices")
    
def Player_status():
  print("-----------------------------------------------------------------------------------")
  print("Weapon 1", Player_status_inventory[2]["weapon_1"])
  print("Weapon 2 ", Player_status_inventory[2]["weapon_2"])
  print("-----------------------------------------------------------------------------------")
  print("Healing Items :", Player_status_inventory[3]["healing_items"])
  print("Healing Uses :", Player_status_inventory[3]["healing_uses"])

  print("Buff_items :", Player_status_inventory[4]["buff_items"])
  print("Buff Uses :", Player_status_inventory[4]["buff_uses"])

  print("Mana Items :", Player_status_inventory[5]["mana_items"])
  print("Mana Uses :", Player_status_inventory[5]["mana_uses"])
  print("-----------------------------------------------------------------------------------")
Player_status()




def Battle():
  print("battle")
  enemy_selection = random.randint(1,3)
  Enemy_selected = Enemy_Mob[enemy_selection]
  Enemy_health = Enemy_selected["health"]
  print("you have encountered a", Enemy_selected["name"])
  print("it has", Enemy_health,"health")
  
  
  print("what will you do?")
  enemy_attack_choice = input("A for begin battle or B to run away").upper()
  if enemy_attack_choice == "A":
    print("you begin to attack")
  elif enemy_attack_choice == "B":
    situation_randomiser()
    
  while Player_status_inventory[0]["health"] > 0 and Enemy_selected["health"] > 0:
    print("what weapon will you use?", Player_status_inventory[2]["weapon_1"]["name"],"(A)", Player_status_inventory[2]["weapon_2"]["name"],"(B)")
    
    weapon_attack_choice = input("---").upper()
    random_attack_generator = random.randrange(0,3,2)
    
    if weapon_attack_choice == "A":
      print("you use your", Player_status_inventory[2]["weapon_1"])
      weapon_damage = Player_status_inventory[2]["weapon_1"]["attack"][random_attack_generator + 1]
    elif weapon_attack_choice == "B":
      print("you use your", Player_status_inventory[2]["weapon_2"])
      weapon_damage = Player_status_inventory[2]["weapon_2"]["attack"][random_attack_generator + 1]
      
    print(weapon_damage)
    Enemy_health -= weapon_damage
    print(Enemy_health)
    if Enemy_health <= 0:
      break
  situation_randomiser()
      
    

def shop():
  print("shop")


def item():
  print("item")

def situation_randomiser():
  Situation_randomiser = random.randint(0,50)
  if Situation_randomiser <= 30:
    Battle()
  elif Situation_randomiser >= 30:
    shop()
  elif Situation_randomiser >= 45:
    item()
situation_randomiser()