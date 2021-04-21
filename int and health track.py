def validate_num_input(user_input):
    while True:
        try:
            num_input = int(input(user_input))
            break
        except ValueError:
            print("Please enter a valid number. ")
    return num_input

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

def print_initiative(init_list):
    print('\nYour initiative order is: ')
    for key in sorted (init_list, reverse=True):
        print('{}: {}'.format(key, ', '.join(init_list[key])))

if __name__ == '__main__':
    init_list = get_initiative()
    print_initiative(init_list)