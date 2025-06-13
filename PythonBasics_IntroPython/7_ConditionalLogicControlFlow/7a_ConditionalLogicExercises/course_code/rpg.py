import random

print("Welcome to the role-playing game!")
player_health = 100
monster_health = 150
heal = 30


def is_factor_of_three(number):
    if number % 3 == 0:
        return True
    else:
        return False


def calculate_damage_dealt_by(attacker):
    if attacker == "player":
        damage = random.randint(10, 15)
    else:  # Monster
        damage = random.randint(15, 20)

    if is_factor_of_three(damage):
        damage = damage * 2
        print(f"💥 {attacker.capitalize()} scored a critical hit of {damage}.")

    return damage


while True:
    print(
        f"❤️ Your health: {player_health}, Monster health: {monster_health}", end="\n\n"
    )

    try:
        action = input("Do you want to (A)ttack, (H)eal, or (R)un away: ")
        action = action.upper()
    except KeyboardInterrupt:
        print("❌ You can't quit the game by pressing Ctrl+C.")
        print("If you really want to leave, you'll need to (R)un...")
        continue

    # Player's turn
    if action == "A":
        damage = calculate_damage_dealt_by("player")
        monster_health -= damage
        print(f"🙂 You attacked the monster for {damage} damage!")

        if monster_health <= 0:
            print("🏆 You defeated the monster!")
            break

    elif action == "H":
        player_health += heal
        if player_health > 100:
            player_health = 100
        print(f"✨ You healed for {heal} health!")

    elif action == "R":
        print("👋 You ran away.")
        break

    else:
        print("❌ Invalid action. Please choose A, H, or R.")
        continue

    # Monster's turn
    if monster_health > 0:
        monster_damage = calculate_damage_dealt_by("monster")
        player_health -= monster_damage
        print(f"🐲 The monster attacked you for {monster_damage} damage!")

        if player_health <= 0:
            print("💀 You were defeated by the monster!")
            break
