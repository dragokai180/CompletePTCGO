from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='d32c8e6b-3a8f-5b02-a431-15c3145fa013',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FightingStadium.Name',
    display_name='Fighting Stadium',
    searchable_by=['Fighting Stadium', 'Stadium', 'FightingStadium'],
    subtypes=['Stadium'],
    collector_number=90,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of each Fighting Pokémon in play (both yours and your opponent's) do 20 more damage to the Defending Pokémon-EX (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The attacks of each Fighting Pokémon in play (both yours and your opponent's) do 20 more damage to the Defending Pokémon-EX (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
