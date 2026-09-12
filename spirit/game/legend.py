"""Physical LEGEND halves form one Pokemon only while paired in play."""
from spirit.game.attributes import AttrID, PokemonStage
from spirit.game.data_utils import def_for


def is_legend(card):
    return card.get_attribute(AttrID.STAGE) == PokemonStage.LEGEND.value


def complementary_halves(first, second):
    if first is second or not is_legend(first) or not is_legend(second):
        return False
    a, b = def_for(first.archetype_id), def_for(second.archetype_id)
    return bool(a and b and a.set_code == b.set_code and a.name == b.name
                and a.collector_number != b.collector_number)


def legend_pairs(cards):
    """Canonical lower-numbered half carries the combined Pokemon's rules."""
    pairs = []
    for index, first in enumerate(cards):
        for second in cards[index + 1:]:
            if complementary_halves(first, second):
                pairs.append(tuple(sorted((first, second), key=lambda card:
                    def_for(card.archetype_id).collector_number)))
    return pairs
