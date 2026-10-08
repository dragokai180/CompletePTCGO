"""Prize-pile queries shared by card effects and game-session actions."""

import random


def face_down_prizes(board, player_id):
    """Return only Prize cards whose faces have not been turned up publicly."""
    area = board.find_player_area(player_id, "prizePile")
    return [card for card in area.children
            if not getattr(card, "publicly_revealed", False)] if area else []


def shuffle_face_down_prizes(board, player_id):
    """Shuffle hidden Prizes without moving cards already turned face up."""
    area = board.find_player_area(player_id, "prizePile")
    if area is None:
        return []
    slots = [index for index, card in enumerate(area.children)
             if not getattr(card, "publicly_revealed", False)]
    cards = [area.children[index] for index in slots]
    random.shuffle(cards)
    for index, card in zip(slots, cards):
        area.children[index] = card
        card.board_slot = index
    return cards
