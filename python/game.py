# Game variables for the hero and villian
hero_name  = "Bizardo the Foolish!"
hero_hp = 100
hero_power = 10 # attack_power

villian_name = "Furgis the Wise"
villian_hp = 500
villian_power = 1

# Drink a health potion
# This increases the hero's hp by 5 points
def drink_health_potion():
  # use global to modify the outside variable
  global hero_hp
  # add to the hero's health
  hero_hp = hero_hp + 5
  print(f"Hero's HP has been increased to {hero_hp}")

# Take a turn
# Allow the user to choose to attack or drink a potion and
# execute the appropriate action
def take_turn():
  # take in the globals
  global villian_hp
  global hero_power
  # get user input (convert to int for easy comparison)
  move = int(input("Press 1 to attack or 2 to take a potion: "))
  if move == 1:
    # attack the villian
    villian_hp = villian_hp - hero_power
    print(f"{villian_name}'s HP has been reduced to {villian_hp}")
  if move == 2:
    drink_health_potion()


def enter_combat():
  global hero_hp
  while True:
    # hero attacks the villian
    take_turn() # hero takes their turn
    # if villian hp <= 0, end loop
    if villian_hp <= 0:
        print(f"Stupidity wins, {hero_name} has prevailed!")
        break

    # villian attacks the hero
    hero_hp = hero_hp - villian_power
    print(f"{villian_name} attacks {hero_name} for {villian_power} damage!")
    print(f"{hero_name}'s HP has been reduced to {hero_hp}")

    # if hero hp <= 0, end loop
    if hero_hp <= 0:
        print(f"You failed, but society didn't, {villian_name} has prevailed")
        break

    print()

enter_combat()