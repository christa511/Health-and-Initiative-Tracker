'''  
This is code that will help a game master/dungeon master get the initiative and health of the players,
put them all in correct initiative order, then help you go through the turns until combat is over.

'''

def validate_num_input(user_input):
    while True:
        try:
            num_input = int(input(user_input))
            break
        except ValueError:
            print("Please enter a valid number. ")
    return num_input
#code for getting initaitive
def get_initiative():
    print('Welcome to Initiative Tracker!')
    initiative_tracking = {}
    for player_name in iter(lambda: input("What is the players name? "), ''):
        player_initiative = validate_num_input('What is {} initiative? '.format(player_name))
        if player_initiative in initiative_tracking:
            initiative_tracking[player_initiative].append(player_name)
        else:
            initiative_tracking[player_initiative] = [player_name]
    return(initiative_tracking)
#code for getting health below
def get_health(newinit):
    initiative = newinit
    health_tracking = {}
    for item in initiative:
        player_health = validate_num_input('What is {} health? '.format(initiative[item]))
        if player_health in health_tracking:
            health_tracking[player_health].append(item)
        else:
            health_tracking[player_health] = initiative[item]
    return(health_tracking)
#code for sorting the list in numerical order
def print_initiative(thisinit):
    print('\nYour initiative order is: ')
    for key in sorted(thisinit, reverse=True):
        print(thisinit[key])

if __name__ == '__main__':
    init_list = get_initiative()
    print_initiative(init_list)
    print(init_list)
    print(get_health(init_list))
    

while True:
    for key in sorted(init_list, reverse=True):
        print("It is", init_list[key], "'s turn.")
        turn_action=input("press A to change health, H to view health, S to skip turn, or L to leave combat. ")
        #removes from players health
        if turn_action.lower() == "a":
            print("you attacked")
            pass
        #add to players health
        elif turn_action.lower() == "h":
            print("you healed")
            pass
        #skips the players turn
        elif turn_action.lower() == "s":
            print("you skipped your turn")
            pass
        #removes the player from the turn order
        elif turn_action.lower() == "l":
            init_list.pop(key)
            break
    if init_list == "":
        print("combat is concluded")
        break
    else:
        pass
