"""Sample adventure"""
import random
def display_player_status(player_health):
    """displays player health"""
    print("Your current health: " + str(player_health))
def handle_path_choice(player_health):
    """chooses path"""
    updated_player_health = player_health
    direction = random.choice(["left, right"])
    if direction == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        updated_player_health += 10
        updated_player_health = min(updated_player_health, 100)
    elif direction == "right":
        print("You fall into a pit and lose 15 health points")
        updated_player_health -= 15
        if updated_player_health < 0:
            print("You are barely alive!")
            updated_player_health = 0
    return updated_player_health
def player_attack(monster_health):
    """You attack"""
    updated_monster_health = monster_health
    print("You strike the monster for 15 damage!")
    updated_monster_health -= 15
    return updated_monster_health

def monster_attack(player_health):
    """Monster attacks"""
    crit = random.random()
    if crit < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        updated_player_health = player_health - 20
    else:
        print("The monster hits you for 10 damage!")
        updated_player_health = player_health - 10
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Simulates combat"""
    updated_player_health = player_health
    updated_monster_health = monster_health
    treasure_found_and_won = False
    while updated_player_health > 0 and updated_monster_health > 0:
        player_attack(updated_monster_health)
        display_player_status(updated_player_health)
        monster_attack(updated_player_health)
        if updated_player_health == 100:
            break
    if updated_player_health <= 0:
        print("Game Over!")
    elif updated_player_health > 0 and check_for_treasure(has_treasure):
        print("You defeated the monster!")
        treasure_found_and_won = True
    return treasure_found_and_won # boolean
def check_for_treasure(has_treasure):
    """check for the treasure"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")
    return has_treasure
def acquire_item(inventory, item):
    """acquire item"""
    list.append(inventory, item)
    print("You acquired a " + item + "!")
    return inventory

def display_inventory(inventory):
    """display inventory"""
    print("Your inventory:")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    invcount = 1
    for i in inventory:
        print(str(invcount) + ". " + str(i))
        invcount += 1
def enter_dungeon(player_health, inventory, dungeon_rooms):
    """simulate dungeon"""
    updated_inventory = inventory
    updated_player_health = player_health
    for i in dungeon_rooms:
        print(i[0])
        if i[1] is not None:
            print("You found a " + i[1] + " in the room.")
            acquire_item(updated_inventory, i[1])
        if i[2] is not None:
            if i[2] == "puzzle":
                choice = input("'solve' or 'skip'") == "solve"
                if choice is True:
                    outcome = random.choice([True, False])
                    if outcome is False:
                        print(i[3][1])
                    else:
                        print(i[3][0])
            else:
                choice = input("'disarm' or 'bypass'") == "disarm"
                if choice is True:
                    outcome = random.choice([True, False])
                    if outcome is False:
                        print(i[3][1])
                    else:
                        print(i[3][0])
        else:
            print("There doesn't seem to be a challenge in this room. You move on.")
        if i[2] is not None:
            updated_player_health += int(i[3][2])
            if updated_player_health > 0:
                print("You are barely alive!")
                updated_player_health = 0
        display_inventory(updated_inventory)
    display_player_status(updated_player_health)
    return updated_player_health, updated_inventory
def main():
    """main"""
    inventory = []
    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle",
     ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap",
     ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None),
    ("A small room with a locked chest", "treasure", "puzzle",
     ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    player_health = 100
    monster_health = 70 # Example hardcoded value
    has_treasure = False

    has_treasure = random.choice([True, False]) # Randomly assign treasure

    player_health = handle_path_choice(player_health)

    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic
    if player_health > 0:
        enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
