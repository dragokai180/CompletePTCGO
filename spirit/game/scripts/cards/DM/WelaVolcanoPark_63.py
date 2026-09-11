from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='dd8595de-b606-5d37-94d8-ce36fbed6758',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WelaVolcanoPark.Name',
    display_name='Wela Volcano Park',
    searchable_by=['Wela Volcano Park', 'Stadium', 'WelaVolcanoPark'],
    subtypes=['Stadium'],
    collector_number=63,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Whenever a player flips a coin for the Special Condition Burned between turns, that Special Condition isn't removed even if the result is heads. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Whenever a player flips a coin for the Special Condition Burned between turns, that Special Condition isn't removed even if the result is heads. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
