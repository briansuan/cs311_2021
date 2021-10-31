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



if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()
    
    # Set cmd line args to my variables
    opp_last = args.last_opponent_move
    rounds = args.iterations
    
    if rounds == 0 or rounds == 99:
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
 





