import argparse
import json  


# BRIAN SUAN
# STRATEGY: 
# My strategy is tit for tat but for the first and last round, always confess, for every round in between, just copy what my opponent's last move was 
# If they confess, I confess, if they stay silent, I stay silent too






# Add last move dictionary to json file
def add_last_move(data):
    my_last_json = json.dumps(data)
    with open('my_last.json', 'w') as f:
        f.write(my_last_json)
    
# Get last move from json file     
def get_my_last():
    with open ('my_last.json', 'r') as f:
        data = json.loads(f.read())
    return data['0']

# update last move dictionary in json file
def update_my_last(move):
    with open ('my_last.json' , 'r') as f:
        data = json.loads(f.read())
        data['0'] = move
    add_last_move(data)


if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()
    
    # Set cmd line args to my variables
    opp_last = args.last_opponent_move
    rounds = args.iterations

    # initialize my_last dictionary 
    my_last = {0 : ''}
    add_last_move(my_last)

    
    if rounds == '0' or rounds == '99':
        current_move = 'confess'
        update_my_last(current_move)
        print(current_move)
    elif opp_last == get_my_last():
        current_move = opp_last
        update_my_last(current_move)
        print(current_move)
    elif opp_last != get_my_last():
        current_move = 'confess'
        update_my_last(current_move)
        print(current_move)

 















