import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(monster):
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass,and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here")
    print_pause("and has been terrifying the near nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty,")
    print_pause("(but not very effective) dagger.")


def house(monster, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock,when the door.")
    print_pause(f"opens and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "magical Sword" not in items:
        print_pause("You feel a bit under-prepared for this,")
        print_pause("what with only having a tiny dagger.")


def fight(monster, items):
    if "magical Sword" in items:
        print_pause(f"As the {monster} moves to attack")
        print_pause("you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand,")
        print_pause("as you brace yourself for the attack.")
        print_pause(f"But the {monster} takes one look")
        print_pause("at your shiny new toy and runs away!")
        print_pause("You have rid the town of the troll.You are victorious!")
        print_pause("GAME OVER")
        play_again()
    elif "magical sword" not in items:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {monster}")
        print_pause("You have been defeated!")
        print_pause("GAME OVER")
        play_again()


def run(monster, items):
    print_pause("You run back into the field. Luckily,")
    print_pause("you don't seem to have been followed.")
    game_process(monster, items)


def cave(monster, items):
    print_pause("You peer cautiously into the cave.")
    if "magical Sword" in items:
        print_pause("You've been here before,")
        print_pause("and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger,")
        print_pause("and take the sword with you.")
        items.append("magical Sword")
        print_pause("You walk back out to the field.")


def play_again():
    again = input("Would you like to play again? (y/n)")
    if 'y' in again:
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif 'n' in again:
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def game_process(monster, items):
    response = input("Enter 1 to knock on the door of the house\n"
                     "Enter 2 to peer into the caven\n"
                     "What would you like to do?\n"
                     "Please enter 1 or 2.)\n")
    if response == '1':
        house(monster, items)
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == '1':
            fight(monster, items)
        elif choice == '2':
            run(monster, items)
    elif response == '2':
        cave(monster, items)
        game_process(monster, items)


def play_game():
    items = []
    monster_list = ["wicked fairie", "pirate", "dragon", "troll"]
    monster = random.choice(monster_list)
    intro(monster)
    game_process(monster, items)


play_game()
