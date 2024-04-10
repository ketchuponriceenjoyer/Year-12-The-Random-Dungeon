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

gem_shards = [{"diamond_shard": False},{"gold_shard": False},{"coal_shard": False},{"emerald_shard": False},{"lapis_shard": False},]

player_status_inventory = [
    {"health": 100},  #0
    {"coins": 0},  #1
    {"weapon_1": None,"weapon_2": None},  #2
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
      break

    elif Chosen_weapon_1 == 2:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_1"] = weapon[1]
      break
      #chosen whip for weapon1

    elif Chosen_weapon_1 == 3:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_1"] = weapon[2]
      break

      #chosen staff for weapon1

  except ValueError:
    print("not in choices")
    continue

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
      
      break

    elif Chosen_weapon_2 == 2:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_2"] = weapon[1]
      
      break
      #chosen whip for weapon1

    elif Chosen_weapon_2 == 3:
      player_status_inventory[1][
          "coins"] = player_status_inventory[1]["coins"] + random.randint(
              5, 10)
      player_status_inventory[2]["weapon_2"] = weapon[2]
      
      
      
      break

  except ValueError:
    print("not in choices")
    continue


def Player_status():
  allow_status_change = False
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

  if allow_status_change == True:
    print("")
  

Player_status()


def battle():
  enemy_selected = enemy_mob[random.randint(1, 3)]
  enemy_use_weapon_or_not = random.randint(1,2)
  enemy_weapon_selection = random.randint(0, 3)
  
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
    print("Players turn")
    print("-----------------------------------------------------------------------------------")
    player_damage_dealt = 0
    print("Choose which weapon you would like to use ot you use an")
    print("(A)", player_status_inventory[2]["weapon_1"]["name"], "(B)")
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
      
    print("-----------------------------------------------------------------------------------")
    print("Result")
    print("-----------------------------------------------------------------------------------")
    enemy_selected["health"] -= player_damage_dealt
    print("you dealt", player_damage_dealt, "Damage")
    if enemy_selected["health"] <= 0:
      print("0 : Health")
    else:
      print(enemy_selected["health"], " : Enemy Health")

    if enemy_selected["health"] <= 0:
      reward = random.randint(5, 25)
      player_status_inventory[1]["coins"] += reward
      print("you have defeated the", enemy_selected["name"])
      print("you have been awarded, ", player_status_inventory[1]["coins"])
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
    print("-----------------------------------------------------------------------------------")
    
def docter():
  medical_cost = random.randint(45,150)
  medical_treatment = random.randint(5,25)
  print("-----------------------------------------------------------------------------------")
  print("You find a small cavern")
  print("you enter the cavern and notice its a man")
  print("the man tells you he's a docter and ask if you need medical attention")
  print("the cost is", medical_cost, "coins")
  print("you have", player_status_inventory[1]["coins"],"coins")
  print("you have", player_status_inventory[0]["health"],": health")
  print("will you need treatment? A for yes B for no")
  while True:
    try:
      shop_keeper_sells = input(":").upper()
      print("")
      if shop_keeper_sells == "A":
        if player_status_inventory[0]["health"] == 100:
          print("you are already max health")
          continue
        else:
          if player_status_inventory[1]["coins"] >= medical_cost:
            player_status_inventory[0]["health"] += medical_treatment
            if player_status_inventory[0]["health"] > 100:
              print("you have been healed up to max health")
              player_status_inventory[0]["health"] = 100
            else:
              print("you have been healed to", player_status_inventory[0]["health"], "health")
              print("Thanks for coming")
              print("you leave the cavern and go on your way")
              situation_randomiser()
          else:
            print("you do not have enough coins")
            continue
            
      elif shop_keeper_sells == "B":
        print("Get the hell out of my cavern!")
        situation_randomiser()
    except ValueError:
      print("not in choices")

def crystal():
  print("item")


def situation_randomiser():
  allow_status_change = True
  Situation_randomiser = random.randint(0, 50)
  if Situation_randomiser <= 35:
    battle()
  elif Situation_randomiser >= 35:
    docter()
  elif Situation_randomiser >= 40:
    crystal()
situation_randomiser()

