def is_high_card(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) != 5:
        return False
    
    min_val = min(card_values)
    for i in range(5):
        card_values[i] = card_values[i] - min_val
    if card_values == [0,1,2,3,4]:
        return False
    
    suit_values = []
    for card in hand:
        suit_values.append(card['suit'])
    if len(set(suit_values)) ==1:
        return False
    
    return True

def is_pair(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) == 4:
        return True
    else:
        return False

def is_2_pair(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) == 3 and (card_values[0] != card_values[2] and card_values[1] != card_values[3] and card_values[2] != card_values[4]):
        return True
    else:
        return False

def is_3_of_a_kind(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) ==3 and (card_values[0] == card_values[2] or card_values[1] == card_values[3] or card_values[2]== card_values[4]):
        return True
    else:
        return False

def is_4_of_a_kind(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) == 2 and (card_values[0] == card_values[3] or card_values[1]== card_values[4]):
        return True
    else:
        return False

def is_full_house(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    if len(set(card_values)) == 2 and (card_values[0] != card_values[3] and card_values[1] != card_values[4]):
        return True 
    else:
        return False

def is_flush(hand):
    suit_values = []
    for card in hand:
        suit_values.append(card['suit'])
    if len(set(suit_values)) > 1:
        return False
    else:
        return True

def is_straight(hand):
    card_values = []
    for card in hand:
        card_values.append(card['value'])
    card_values.sort()
    min_val = min(card_values)
    for i in range(5):
        card_values[i] = card_values[i] - min_val
    if card_values != [0,1,2,3,4]:
        return False
    else:
        return True

def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False