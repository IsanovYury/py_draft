def winner(deck_steve, deck_josh):
    my_list = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    i = 0 
    deck_steve_p, deck_josh_p = 0, 0
    while len(deck_steve) > 0 and len(deck_josh) > 0:
        if my_list.index(deck_steve[i]) > my_list.index(deck_josh[i]):
            deck_steve_p += 1
        elif my_list.index(deck_steve[i]) < my_list.index(deck_josh[i]):
            deck_josh_p += 1
        deck_steve.pop(i)
        deck_josh.pop(i)
    if deck_steve_p > deck_josh_p:
        return f"Steve wins {deck_steve_p} to {deck_josh_p}"
    elif deck_steve_p < deck_josh_p:
        return f"Josh wins {deck_josh_p} to {deck_steve_p}"
    else:
        return 'Tie'
