def play_pocker(cards):
    cards_set = set(cards)
    jokers = cards.count(0)
    max_length = 0

    for card in cards_set:
        if card != 0 and card - 1 not in cards_set:
            current_length = 1
            current_card = card + 1
            available_jokers = jokers

            while current_card in cards_set or available_jokers > 0:
                if current_card not in cards_set:
                    available_jokers -= 1
                current_length += 1
                current_card += 1

            max_length = max_length if max_length > current_length else current_length

    return max_length
