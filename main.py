import time
import random

weapon = [
    {
        "name": "sword",
        "attack": {
            "first_name": "light_attack",
            "first_skill": random.randint(5, 10),
            "second_name": "heavy_attack",
            "second_skill": random.randint(10, 15)
        }
    },  # 0
    {
        "name": "whip",
        "attack": {
            "first_name": "strike",
            "first_skill": random.randint(3, 4),
            "second_name": "rip",
            "second_skill": random.randint(4, 12)
        }
    },  # 1
    {
        "name": "staff",
        "attack": {
            "first_name": "fireball",
            "first_skill": random.randint(10, 17),
            "second_name": "lightning Strike",
            "second_skill": random.randint(20, 28)
        }
    },  # 2
    {
        "name": "bow",
        "attack": {
            "first_name": "light arrow",
            "first_skill": random.randint(5, 10),
            "second_name": "piercing arrow",
            "second_skill": random.randint(1, 4)
        }
    }  # 2
]

healing_items = [
    {
        "name": None,
        "health_giver": None
    },
    {
        "name": "herbs",
        "health_giver": random.randint(5, 10)
    },
    {
        "name": "health_potion",
        "health_giver": random.randint(18, 25)
    },
    {
        "name": "big_healing_potion",
        "health_giver": random.randint(28, 36)
    },
    {
        "name": "large_healing_potion",
        "health_giver": 50
    },
    {
        "name": "pie",
        "health_giver": 100
    },
]

mana_items = [
    {
        "name": None,
        "mana_giver": None
    },
    {
        "name": "blueberry",
        "mana_giver": random.randint(5, 10)
    },
    {
        "name": "mana_potion",
        "mana_giver": random.randint(18, 25)
    },
    {
        "name": "big_mana_potion",
        "mana_giver": random.randint(28, 36)
    },
    {
        "name": "large_mana_potion",
        "mana_giver": 50
    },
    {
        "name": "blueberry_Pie",
        "mana_giver": 100
    },
]

buff_items = [
    {
        "name": None,
        "attack_boost": None
    },
    {
        "name": "Magic_Meat_Rib",
        "attack_boost": random.randint(5, 10)
    },
    {
        "name": "strength_potion",
        "attack_boost": random.randint(18, 25)
    },
    {
        "name": "Big_strength_potion",
        "attack_boost": random.randint(28, 36)
    },
    {
        "name": "large_strength_potion",
        "attack_boost": 50
    },
    {
        "name": "Chug_Chug",
        "attack_boost": 100
    },
]

enemy_mob = [
    {
        "name": "nobody",
        "attack": "nothing"
    },
    {
        "name": "goblin",
        "health": random.randint(5, 10),
        "attack": {
            "first_name": "jab",
            "first_skill": random.randint(5, 10),
            "second_name": "roundhouse",
            "second_skill": random.randint(10, 20)
        }
    },
    {
        "name": "orc",
        "health": random.randint(10, 20),
        "attack": {
            "first_name": "boulder throw",
            "first_skill": random.randint(8, 15),
            "second_name": "shoulder strike",
            "second_skill": random.randint(24, 30)
        }
    },
    {
        "name": "giant",
        "health": random.randint(20, 30),
        "attack": {
            "first_name": "smash",
            "first_skill": random.randint(15, 20),
            "second_name": "stomp",
            "second_skill": random.randint(30, 40)
        }
    },
]

crystals = []

player_status_inventory = [
    {
        "health": 100,
        "mana": 50
    },  #0
    {
        "coins": 0
    },  #1
    {
        "weapon_1": None,
        "weapon_2": None
    },  #2
    {
        "healing_items":
        [healing_items[0], healing_items[0], healing_items[0]],
        "healing_uses": [0, 0, 0]
    },  #3
    {
        "buff_items": [buff_items[0], buff_items[0], buff_items[0]],
        "buff_uses": [0, 0, 0]
    },  #4
    {
        "mana_items": [mana_items[0], mana_items[0], mana_items[0]],
        "mana_uses": [0, 0, 0]
    },  #5
]

print("Welcome to the The Random Dungeon Game")
#time.sleep(3.5)
print(
    "In this game you wake up lost in a mysterious forest and is looking for a way out"
)
#time.sleep(3.5)
print(
    "you have a nothing in your inventory but see skeletal corpses on the ground"
)
#time.sleep(3.5)
print("But on those corpses they appear to have a")
#time.sleep(1.4)
print(weapon[0]["name"])
#time.sleep(1.4)
print(weapon[1]["name"])
#time.sleep(1.4)
print(weapon[2]["name"])
print("you can only pick 2 weapons")
#time.sleep(3.5)
print("weapon choices", " 1 for sword", " 2 for Whimp", " 3 for staff")
#time.sleep(2.5)

while True:
  try:
    Chosen_weapon_1 = int(input("Choose your first weapon -- "))
    #chosen sword for weapon1
    if Chosen_weapon_1 == 1:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_1"] = weapon[0]
      player_status_inventory[3]["healing_items"][0] = healing_items[1]
      player_status_inventory[3]["healing_uses"][0] = random.randint(3, 6)
      player_status_inventory[4]["buff_items"][0] = buff_items[1]
      player_status_inventory[4]["buff_uses"][0] = random.randint(1, 4)
      break

    elif Chosen_weapon_1 == 2:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_1"] = weapon[1]
      player_status_inventory[3]["healing_items"][0] = healing_items[1]
      player_status_inventory[3]["healing_uses"][0] = random.randint(4, 8)
      break
      #chosen whip for weapon1

    elif Chosen_weapon_1 == 3:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_1"] = weapon[2]
      player_status_inventory[3]["healing_items"][0] = healing_items[1]
      player_status_inventory[3]["healing_uses"][0] = random.randint(4, 8)
      player_status_inventory[5]["mana_items"][0] = mana_items[1]
      player_status_inventory[5]["mana_uses"][0] = random.randint(4, 8)
      break

      #chosen staff for weapon1

  except ValueError:
    print("not in choices")

while True:
  try:
    Chosen_weapon_2 = int(input("Choose your second weapon -- "))

    if Chosen_weapon_1 == Chosen_weapon_2:
      print("cannot pick the same weapon")
      continue
      #chosen sword for weapon1
    if Chosen_weapon_2 == 1:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_2"] = weapon[0]
      player_status_inventory[3]["healing_items"][1] = healing_items[1]
      player_status_inventory[3]["healing_uses"][1] = random.randint(3, 6)
      player_status_inventory[4]["buff_items"][1] = buff_items[1]
      player_status_inventory[4]["buff_uses"][1] = random.randint(1, 4)
      break

    elif Chosen_weapon_2 == 2:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_2"] = weapon[1]
      player_status_inventory[3]["healing_items"][1] = healing_items[1]
      player_status_inventory[3]["healing_uses"][1] = random.randint(4, 8)
      break
      #chosen whip for weapon1

    elif Chosen_weapon_2 == 3:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_2"] = weapon[2]
      player_status_inventory[3]["healing_items"][1] = healing_items[1]
      player_status_inventory[3]["healing_uses"][1] = random.randint(4, 8)
      player_status_inventory[5]["mana_items"][1] = mana_items[1]
      player_status_inventory[5]["mana_uses"][1] = random.randint(4, 8)
      break

  except ValueError:
    print("not in choices")


def Player_status():
  print(
      "-----------------------------------------------------------------------------------"
  )
  print("Weapon 1 :", player_status_inventory[2]["weapon_1"]["name"],
        "| First skill(",
        player_status_inventory[2]["weapon_1"]["attack"]["first_name"],
        ") : deals[",
        player_status_inventory[2]["weapon_1"]["attack"]["first_skill"], "] |",
        " Second skill(",
        player_status_inventory[2]["weapon_1"]["attack"]["second_name"],
        ") : deals[",
        player_status_inventory[2]["weapon_1"]["attack"]["second_skill"], "]")
  print()
  print(player_status_inventory[1]["coins"], "coins")
  print()
  print("Weapon 2 :", player_status_inventory[2]["weapon_2"]["name"],
        "| First skill(",
        player_status_inventory[2]["weapon_2"]["attack"]["first_name"],
        ") : deals[",
        player_status_inventory[2]["weapon_2"]["attack"]["first_skill"], "] |",
        " Second skill(",
        player_status_inventory[2]["weapon_2"]["attack"]["second_name"],
        ") : deals[",
        player_status_inventory[2]["weapon_2"]["attack"]["second_skill"], "]")
  print(
      "-----------------------------------------------------------------------------------"
  )
  print("Healing Items :", "Slot 1 (",
        player_status_inventory[3]["healing_items"][0]["name"], ") |",
        "Slot 2 (", player_status_inventory[3]["healing_items"][1]["name"],
        ") |", "Slot 3 (",
        player_status_inventory[3]["healing_items"][2]["name"], ")")
  print("Healing Uses :", "Slots 1 (",
        player_status_inventory[3]["healing_uses"][0], ") |", "Slots 2 (",
        player_status_inventory[3]["healing_uses"][1], ") |", "Slots 3 (",
        player_status_inventory[3]["healing_uses"][2], ")")
  print()
  print("Buff_items :", "Slot 1 (",
        player_status_inventory[4]["buff_items"][0]["name"], ") |", "Slot 2 (",
        player_status_inventory[4]["buff_items"][1]["name"], ") |", "Slot 3 (",
        player_status_inventory[4]["buff_items"][2]["name"])
  print("Buff Uses :", "Slots 1 (", player_status_inventory[4]["buff_uses"][0],
        ") |", "Slots 2 (", player_status_inventory[4]["buff_uses"][1], ") |",
        "Slots 3 (", player_status_inventory[4]["buff_uses"][2], ")")
  print()
  print("Mana Items :", "Slot 1 (",
        player_status_inventory[5]["mana_items"][0]["name"], ") |", "Slot 2 (",
        player_status_inventory[5]["mana_items"][1]["name"], ") |", "Slot 3 (",
        player_status_inventory[5]["mana_items"][2]["name"], ")")
  print("Mana Uses :", "Slots 1 (", player_status_inventory[5]["mana_uses"][0],
        ") |", "Slots 2 (", player_status_inventory[5]["mana_uses"][1], ") |",
        "Slots 3 (", player_status_inventory[5]["mana_uses"][2], ")")
  print(
      "-----------------------------------------------------------------------------------"
  )


Player_status()


def battle():
  enemy_selected = enemy_mob[random.randint(1, 3)]
  enemy_use_weapon_or_not = random.randint(1,2)
  enemy_weapon_selection = random.randint(0, 3)
  print("Players turn")
  print("-----------------------------------------------------------------------------------")
  print("you have encountered a", enemy_selected["name"])
  print(enemy_selected["health"], " : Health")
  
  if enemy_use_weapon_or_not == 1:
    enemy_selected["attack"] = weapon[enemy_weapon_selection]
    print("It is using :", enemy_selected["attack"]["name"])
    print(enemy_selected["attack"]["attack"]["first_name"], " : deals", enemy_selected["attack"]["attack"]["first_skill"],"damage")
    print(enemy_selected["attack"]["attack"]["second_name"], " : deals", enemy_selected["attack"]["attack"]["second_skill"],"damage")
  elif enemy_use_weapon_or_not == 2:
    print(enemy_selected["attack"]["first_name"], " : deals", enemy_selected["attack"]["first_skill"],"damage")
    print(enemy_selected["attack"]["second_name"], " : deals", enemy_selected["attack"]["second_skill"],"damage")
  print("-----------------------------------------------------------------------------------")
  while True:
    try:
      attack_enemy_choice = input("A for begin battle or B to run away").upper()
      if attack_enemy_choice == "A":
        print("you begin to attack")
        break
      elif attack_enemy_choice == "B":
        print("you chose to run away")
        situation_randomiser()
    except ValueError:
      print("not in choices")
    

  while True:
    player_damage_dealt = 0
    print("Choose which weapon you would like to use")
    print(("(A)", player_status_inventory[2]["weapon_1"]["name"], "(B)", player_status_inventory[2]["weapon_2"]["name"]))
    player_weapon_selection_choice = input(":  ").upper()
    if player_weapon_selection_choice == "A":
      weapon_skill_selection = random.randint(1,2)
      if weapon_skill_selection == 1:
        player_damage_dealt = player_status_inventory[2]["weapon_1"]["attack"]["first_skill"]
        print("You use", player_status_inventory[2]["weapon_1"]["name"], "skill(",player_status_inventory[2]["weapon_1"]["attack"]["first_skill"],")", player_status_inventory[2]["weapon_1"]["attack"]["first_name"])
      if weapon_skill_selection == 2:
        player_damage_dealt = player_status_inventory[2]["weapon_1"]["attack"]["second_skill"]
        print("You use", player_status_inventory[2]["weapon_1"]["name"], "skill(",player_status_inventory[2]["weapon_1"]["attack"]["second_skill"],")", player_status_inventory[2]["weapon_1"]["attack"]["second_name"])
        
    elif player_weapon_selection_choice == "B":
      weapon_skill_selection = random.randint(1,2)
      if weapon_skill_selection == 1:
        player_damage_dealt = player_status_inventory[2]["weapon_2"]["attack"]["first_skill"]
        print("You use", player_status_inventory[2]["weapon_2"]["name"], "skill(",player_status_inventory[2]["weapon_2"]["attack"]["first_skill"],")", player_status_inventory[2]["weapon_2"]["attack"]["first_name"])
      if weapon_skill_selection == 2:
        player_damage_dealt = player_status_inventory[2]["weapon_2"]["attack"]["second_skill"]
        print("You use", player_status_inventory[2]["weapon_2"]["name"], "skill(",player_status_inventory[2]["weapon_2"]["attack"]["second_skill"],")", player_status_inventory[2]["weapon_2"]["attack"]["second_name"])
    else:
      print("not in choices")
      continue
      
    enemy_selected["health"] -= player_damage_dealt
    print("you dealt", player_damage_dealt, "Damage")
    if enemy_selected["health"] <= 0:
      print("0 : Health")
    else:
      print(enemy_selected["health"], " : Enemy Health")

    if enemy_selected["health"] <= 0:
      print("you have defeated the", enemy_selected["name"])
      situation_randomiser()
      break


    enemy_damage_dealt = 0
    if enemy_use_weapon_or_not == 1:
      enemy_weapon_skill_selection = random.randint(1,2)
      if enemy_weapon_skill_selection == 1:
        enemy_damage_dealt = enemy_selected["attack"]["attack"]["first_skill"]
        print("The enemy uses", enemy_selected["attack"]["attack"]["first_name"], "skill(",enemy_selected["attack"]["attack"]["first_skill"],")")
      if enemy_weapon_skill_selection == 2:
        enemy_damage_dealt = enemy_selected["attack"]["attack"]["second_skill"]
        print("The enemy uses", enemy_selected["attack"]["attack"]["second_name"], "skill(",enemy_selected["attack"]["attack"]["second_skill"],")")
    if enemy_use_weapon_or_not == 2:
      enemy_weapon_skill_selection = random.randint(1,2)
      if enemy_weapon_skill_selection == 1:
        enemy_damage_dealt = enemy_selected["attack"]["first_skill"]
        print("The enemy uses", enemy_selected["attack"]["first_name"], "skill(",enemy_selected["attack"]["first_skill"],")")
      if enemy_weapon_skill_selection == 2:
        enemy_damage_dealt = enemy_selected["attack"]["second_skill"]
        print("The enemy uses", enemy_selected["attack"]["second_name"], "skill(",enemy_selected["attack"]["second_skill"],")")

    player_status_inventory[0]["health"] -= enemy_damage_dealt
    print("The enemy dealt", enemy_damage_dealt, "Damage")
    if player_status_inventory[0]["health"] <= 0:
      print("You Died")
      break
    else:
      print(player_status_inventory[0]["health"], " : Your Health")
  
def shop():

  print("shop")
  enemy_attack_choice = input("A for begin battle or B to run away").upper()
  if enemy_attack_choice == "A":
    print("you begin to attack")
  elif enemy_attack_choice == "B":
    situation_randomiser()


def item():
  print("item")


def situation_randomiser():
  Situation_randomiser = random.randint(0, 50)
  if Situation_randomiser <= 30:
    battle()
  elif Situation_randomiser >= 30:
    shop()
  elif Situation_randomiser >= 40:
    item()


situation_randomiser()
