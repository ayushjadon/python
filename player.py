


working_hours = [('ayu',200),('suhas',250),('nemo',500)]





list_jug = ['','0','']
from random import shuffle
shuffle(list_jug)
print(list_jug)


from random import randint


class Door(object):


    def __init__(self, has_car):
        self.has_car = has_car

    def whats_behind(self):

        return 'car' if self.has_car else 'goat'


def pick_random_door(num_doors):

    return randint(0, num_doors - 1)


def create_doors(num_doors=3):

    doors = []
    car_index = pick_random_door(num_doors)
    for i in range(0, num_doors):
        doors.append(Door(car_index == i))

    return doors, car_index


def run_game(switch=False, num_doors=3):

    assert(num_doors >= 3)


    doors, car_at = create_doors(num_doors)

    # Let the player randomly select a door.
    player_choice = pick_random_door(num_doors)


    host_choice = car_at
    while host_choice == player_choice or host_choice == car_at:
        host_choice = pick_random_door(num_doors)


    assert(doors[host_choice].whats_behind() == 'goat')


    if switch:
        old_player_choice = player_choice
        player_choice = old_player_choice
        while player_choice == old_player_choice or player_choice == host_choice:
            player_choice = pick_random_door(num_doors)


    return doors[player_choice].whats_behind() == 'car'


def run_multiple_games(num_games=1, num_doors=3):

    assert(num_games >= 1)
    games_won_stayed = 0
    games_won_switched = 0
    for i in range(0, num_games):

        if run_game(False, num_doors=num_doors):
            games_won_stayed += 1


        if run_game(True, num_doors=num_doors):
            games_won_switched += 1

    print('player run: %d' % num_games)
    print('player won stayed: %d' % games_won_stayed)
    print('player won switched: %d' % games_won_switched)

run_multiple_games(num_games=2000, num_doors=4)



