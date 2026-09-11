from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='915776f2-92b4-53ab-97ad-bcf2d4ce25a9',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DimensionValley.Name',
    display_name='Dimension Valley',
    searchable_by=['Dimension Valley', 'Stadium', 'DimensionValley'],
    subtypes=['Stadium'],
    collector_number=93,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Psychic Pokémon's attacks (both yours and your opponent's) cost Colorless less. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Psychic Pokémon's attacks (both yours and your opponent's) cost Colorless less. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
