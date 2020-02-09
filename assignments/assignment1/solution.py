import json 


def check_valid(current_pairs):
    taken_men = set()
    for _, m in current_pairs:
        if m in taken_men:
            return False 
        taken_men.add(m)
    return True 


def solve_helper(preferences, current_pairs, current_index, num_women):
    # see if we can progress (i.e. not at a deadend)
    if not check_valid(current_pairs):
        return False 
    # we hit a solution!
    if current_index == num_women:
        return True 
    current_preferences = preferences[current_index]
    # iterate over possible actions
    for possible_husband in current_preferences:
        # take an action
        current_pairs.append((current_index, possible_husband))
        # see if this action takes us to a solution
        if solve_helper(preferences, current_pairs, current_index + 1, num_women):
            return True 
        # reach here only if we hit a deadend because of this action, so we undo it
        current_pairs.pop(-1)
    # we made a mistake higher up, we need to undo it
    return False 

def solve(preferences, num_women):
    current_pairs = []
    current_index = 0
    solve_helper(preferences, current_pairs, current_index, num_women)
    return current_pairs


def fix_preferences(preferences):
    p1 = {}
    for k, v in preferences.items():
        p1[int(k)] = list(map(int, v))
    return p1


def main():
    with open('prefs.json') as fp:
        content = json.load(fp)
        preferences = fix_preferences(content['preferences'])
        num_women = int(content['num_women'])
        pairs = solve(preferences, num_women)
        if not pairs:
            print('No solution!')
        else:
            print('Solution found!')
            print(pairs)





if __name__ == "__main__":
    main()
            
