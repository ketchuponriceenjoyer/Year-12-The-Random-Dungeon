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
            "first_skill": random.randint(5, 17),
            "second_name": "lightning Strike",
            "second_skill": random.randint(5, 20)
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
        "attack": {
          "mob_first_name": None,
          "mob_first_skill": random.randint(5, 10),
          "mob_second_name": "roundhouse",
          "mob_second_skill": random.randint(10, 20)
      }
    },
    {
        "name": "goblin",
        "health": random.randint(20, 35),
        "attack": {
            "mob_first_name": "jab",
            "mob_first_skill": random.randint(5, 10),
            "mob_second_name": "roundhouse",
            "mob_second_skill": random.randint(10, 20)
        }
    },
    {
        "name": "orc",
        "health": random.randint(30, 40),
        "attack": {
            "mob_first_name": "boulder_throw",
            "mob_first_skill": random.randint(8, 15),
            "mob_second_name": "shoulder_strike",
            "mob_second_skill": random.randint(24, 30)
        }
    },
    {
        "name": "giant",
        "health": random.randint(40, 50),
        "attack": {
            "mob_first_name": "smash",
            "mob_first_skill": random.randint(15, 20),
            "mob_second_name": "stomp",
            "mob_second_skill": random.randint(30, 40)
        }
    },
]
battles_won = 0
gem_shards = [
  {"diamond_shard": False,"name": "diamond_shard"},
  {"gold_shard": False,"name": "gold_shard"},
  {"emerald_shard": False,"name": "emerald_shard"}
]

player_status_inventory = [
    {"health": 100},  #0
    {"coins": 0},  #1
    {"weapon_1": None,"weapon_2": None},  #2
]
def start_game():
  print("Welcome to the The Random Dungeon Game")
  #time.sleep(3.5)
  print("In this game, you find yourself waking up in a mysterious forest and searching for an escape route.")
  #time.sleep(3.5)
  print(
      "you have nothing in your inventory but see skeletal corpses on the ground"
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
start_game()

def Player_status():
  print("-----------------------------------------------------------------------------------")
  print("                          -PLAYER STATS AND INVENTORY-                                    ")
  print("-----------------------------------------------------------------------------------")
  print()
  print("Health:", player_status_inventory[0]["health"])
  print()
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
  print("-----------------------------------------------------------------------------------")
  print("Gem shards - ")
  if gem_shards[0]["diamond_shard"] == True:
    print("Diamond Shard")
  if gem_shards[1]["gold_shard"] == True:
    print("Gold Shard")
  if gem_shards[2]["emerald_shard"] == True:
    print("Emerald Shard")
  

Player_status()

def on_game_check_status():
  while True:
    try:
      print("before you enter the next event, would you like to check your status? A for yes B for no or C for reset game")
      player_options = input(":").upper()
      if player_options == "A":
        Player_status()
        situation_randomiser()
        break
      elif player_options == "B":
        situation_randomiser()
      elif player_options == "C":
        start_game()
    except ValueError:
      print("not in choices")

def battle():
  global enemy_mob 
  global weapon
  enemy_selected = enemy_mob[random.randint(1, 3)]
  enemy_use_weapon_or_not = random.randint(1,2)
  enemy_weapon_selection = random.randint(0, 3)
  #Sometimes the enemy will have a health lower than zero for some reason so I added this for a backup just in case the enemy_mob mob fails to give it a good emount of health, this function will decide its health
  if enemy_selected["health"] <= 0:
    enemy_selected["health"] = random.randint(20, 35)
  print("-----------------------------------------------------------------------------------")
  print("                                -BATTLE ENCOUNTER-                                    ")
  print("-----------------------------------------------------------------------------------")
  print("you have encountered a", enemy_selected["name"])
  print(enemy_selected["health"], " : Health")
  
  if enemy_use_weapon_or_not == 1:
    enemy_selected["attack"] = weapon[enemy_weapon_selection]
    print("It is using :", enemy_selected["attack"]["name"])
    print(enemy_selected["attack"]["attack"]["first_name"], " : deals", enemy_selected["attack"]["attack"]["first_skill"],"damage")
    print(enemy_selected["attack"]["attack"]["second_name"], " : deals", enemy_selected["attack"]["attack"]["second_skill"],"damage")
  elif enemy_use_weapon_or_not == 2:
    print(enemy_selected["attack"]["mob_first_name"], " : deals", enemy_selected["attack"]["mob_first_skill"],"damage")
    print(enemy_selected["attack"]["mob_second_name"], " : deals", enemy_selected["attack"]["mob_second_skill"],"damage")
  else:
    print("Theres your problem")
  
  print("-----------------------------------------------------------------------------------")
  while True:
    try:
      attack_enemy_choice = input("A for begin battle or B to run away").upper()
      if attack_enemy_choice == "A":
        print("you begin to attack")
        break
      elif attack_enemy_choice == "B":
        print("you chose to run away")
        on_game_check_status()
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
      print("-----------------------------------------------------------------------------------")
      print("Result")
      print("-----------------------------------------------------------------------------------")
      if weapon_skill_selection == 1:
        player_damage_dealt = player_status_inventory[2]["weapon_1"]["attack"]["first_skill"]
        print("You use", player_status_inventory[2]["weapon_1"]["name"], "skill(",player_status_inventory[2]["weapon_1"]["attack"]["first_skill"],")", player_status_inventory[2]["weapon_1"]["attack"]["first_name"])
      if weapon_skill_selection == 2:
        player_damage_dealt = player_status_inventory[2]["weapon_1"]["attack"]["second_skill"]
        print("You use", player_status_inventory[2]["weapon_1"]["name"], "skill(",player_status_inventory[2]["weapon_1"]["attack"]["second_skill"],")", player_status_inventory[2]["weapon_1"]["attack"]["second_name"])
        
    elif player_weapon_selection_choice == "B":
      print("-----------------------------------------------------------------------------------")
      print("Result")
      print("-----------------------------------------------------------------------------------")
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
      enemy_use_weapon_or_not = 0
      enemy_weapon_selection = 0
      reward = random.randint(5, 25)
      player_status_inventory[1]["coins"] += reward
      print("you have defeated the", enemy_selected["name"])
      print("you have been awarded, ", player_status_inventory[1]["coins"])
      on_game_check_status()
      break


    enemy_damage_dealt = 0
    if enemy_use_weapon_or_not == 1:
      enemy_weapon_skill_selection = random.randint(1,2)
      if enemy_weapon_skill_selection == 1:
        enemy_damage_dealt = enemy_selected["attack"]["attack"]["first_skill"]
        print("The enemy uses", enemy_selected["attack"]["attack"]["first_name"], "skill(",enemy_selected["attack"]["attack"]["first_skill"],")")
      elif enemy_weapon_skill_selection == 2:
        enemy_damage_dealt = enemy_selected["attack"]["attack"]["second_skill"]
        print("The enemy uses", enemy_selected["attack"]["attack"]["second_name"], "skill(",enemy_selected["attack"]["attack"]["second_skill"],")")
    if enemy_use_weapon_or_not == 2:
      enemy_weapon_skill_selection = random.randint(1,2)
      if enemy_weapon_skill_selection == 1:
        enemy_damage_dealt = enemy_selected["attack"]["mob_first_skill"]
        print("The enemy uses", enemy_selected["attack"]["mob_first_name"], "skill(",enemy_selected["attack"]["mob_first_skill"],")")
      elif enemy_weapon_skill_selection == 2:
        enemy_damage_dealt = enemy_selected["attack"]["mob_second_skill"]
        print("The enemy uses", enemy_selected["attack"]["mob_second_name"], "skill(",enemy_selected["attack"]["mob_second_skill"],")")

    player_status_inventory[0]["health"] -= enemy_damage_dealt
    print("The enemy dealt", enemy_damage_dealt, "Damage")
    if player_status_inventory[0]["health"] <= 0:
      print()
      print("You Died")
      print()
      while True:
        try:
          reset_game_choice = input("Would you like to reset the game? A for yes or B for no").upper()
          if reset_game_choice == "A":
            player_status_inventory[0]["health"] = 100
            player_status_inventory[1]["coins"] = 0
            player_status_inventory[2]["weapon_1"] = None
            player_status_inventory[2]["weapon_2"] = None
            start_game()
            break
      
          
          elif reset_game_choice == "b":
            print("Thanks for playing")
            break  
        except ValueError:
          print("not in choices")
    else:
      print(player_status_inventory[0]["health"], " : Your Health")
    print("-----------------------------------------------------------------------------------")



def doctor():
  medical_cost = random.randint(35,100)
  medical_treatment = random.randint(5,35)
  print("-----------------------------------------------------------------------------------")
  print("You find a small cavern")
  print("you enter the cavern and notice its a man")
  print("the man tells you he's a doctor and ask if you need medical attention")
  print("the cost is", medical_cost, "coins")
  print("you have", player_status_inventory[1]["coins"],"coins")
  print("you have", player_status_inventory[0]["health"],": health")
  print("will you need treatment? A for yes B for no or C for information")
  while True:
    try:
      doctor_treatment_choice = input(":").upper()
      print("")
      if doctor_treatment_choice == "A":
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
              on_game_check_status()
          else:
            print("you do not have enough coins")
            continue
            
      elif doctor_treatment_choice == "B":
        print("Get the hell out of my cavern!")
        on_game_check_status()
      elif doctor_treatment_choice == "C":
        print("three gems shards are scattered around the forest and legends say that they are the only way to escape the forest")
        print("If you get all three, an escape to the outside plains will appear")
        print("But you will need run quick though because these creatures are attracted to those shards")
    except ValueError:
      print("not in choices")
      

def crystal_end():
  gem_selection = random.randint(0, 2)
  
  print("-----------------------------------------------------------------------------------")
  if gem_selection == 0:
    gem_shards[gem_selection]["diamond_shard"] = True
  elif gem_selection == 1:
    gem_shards[gem_selection]["gold_shard"] = True
  elif gem_selection == 2:
    gem_shards[gem_selection]["emerald_shard"] = True
    
  if gem_shards[2]["emerald_shard"] or gem_shards[1]["gold_shard"] or gem_shards[0]["diamond_shard"] == True:
    gem_selection = random.randint(0, 3)

  print("you found a ", gem_shards[gem_selection]["name"])
  print("-----------------------------------------------------------------------------------")
  if gem_shards[2]["emerald_shard"] and gem_shards[1]["gold_shard"] and gem_shards[0]["diamond_shard"] == True:
    print("-----------------------------------------------------------------------------------")
    print("you have found all the gem shards")
    print("you run as fast as you can, as you see mobs jump out of any direction, trying to get you")
    print("you see light coming from your direction and far ahead you see a full plain area where no trees are found")
    print("you escape out of the forest as the enemies can no longer get you as you see them standing inside the shade of the trees")
    print("you realise they are the cursed creatures that have been stuck in the forest for centuries")
    print("you leave with full relief but you suddnely fall asleep")
    print("you wake up inside the forest again not remembering a single thing of what happend")
    print("you look around and see corpses lying on the ground with three weapons")
    print("it starts all over again as the forest has now cursed you just like the rest of us")
    print("-----------------------------------------------------------------------------------")
    print("THE END")
    print("Thanks to anyone who has been playing my game till the end have a great day")
    while True:
      try:
        player_end_choice = input("Would you like to play again? A for yes B for no").upper()
        if player_end_choice == "A":
          start_game()
          break
        else:
          print("Thanks for playing")
          break
      except ValueError:
        print("not in choices")
    
  else:
    on_game_check_status()
    
    
  

def situation_randomiser():
  
  Situation_randomiser = random.randint(0, 45)

  
  if Situation_randomiser >= 45:
    crystal_end()
  elif Situation_randomiser > 40:
    doctor()
  elif Situation_randomiser <= 40:
    battle()
  if gem_shards[2]["emerald_shard"] and gem_shards[1]["gold_shard"] and gem_shards[0]["diamond_shard"] == True:
    crystal_end()
situation_randomiser()

