import argparse
import json  



# Add last moves dictionary to json file
def add_last_move(data, filename='my_last.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)
    
# Get last moves from json file     
def load_last_move(move):
    with open ('my_last.json') as json_file:
        data = json.load(json_file)
        data[0] = move
    add_last_move(data)

# View my last moves
def view_my_last():
    with open ('my_last.json') as json_file:
        data = json.load(json_file)
    return data

# Add cooperation counter dict to json file
def load_coop_cntr(data):
    with open ('coop_cntr.json', 'w') as f:
        json.dump(data, f)

# View cooperation counter
def view_coop_cntr():
    with open ('coop_cntr.json', 'w') as f:
        data = json.load(json_file)
        coop = data[0]
    return coop



if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()
    
    # Set cmd line args to my variables
    opp_last = args.last_opponent_move
    #rounds = args.iterations 
    
    if args.iterations == 0 or args.iterations == 99:
        current_move = 'silent'
        my_prev = {0 : current_move}
        add_last_move(my_prev)
        print(current_move)
    elif opp_last == view_my_last():
        load_last_move(opp_last)
        print(opp_last)
    elif opp_last != view_my_last():
        current_move = 'confess'
        load_last_move(current_move)
        print(current_move)
 





