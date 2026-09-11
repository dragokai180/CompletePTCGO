from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='c6c72ca5-6e31-5b00-a99d-cee00ca1c061',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MountainRing.Name',
    display_name='Mountain Ring',
    searchable_by=['Mountain Ring', 'Stadium', 'MountainRing'],
    subtypes=['Stadium'],
    collector_number=97,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to Benched Pokémon by attacks (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Prevent all damage done to Benched Pokémon by attacks (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
