def get_coin_balances(lst1, lst2):
    person_one_coins = 3
    person_two_coins = 3
    for action_p1, action_p2 in zip(lst1, lst2):
        if action_p1 == "share":
            if action_p2 == "share":
                person_one_coins += 2
                person_two_coins += 2
            elif action_p2 == "steal":
                person_one_coins -= 1
                person_two_coins += 3
        elif action_p1 == "steal":
            if action_p2 == "share":
                person_one_coins += 3
                person_two_coins -= 1
    
    return person_one_coins, person_two_coins