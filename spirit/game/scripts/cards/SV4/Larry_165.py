from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='07e872bc-8e5b-51d7-94cb-8af6a7f5bfe4',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Larry.Name',
    display_name='Larry',
    searchable_by=['Larry', 'Supporter', 'Larry'],
    subtypes=['Supporter'],
    collector_number=165,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect('Flip a coin. If heads, search your deck for up to 2 Pokémon, reveal them, and put them into your hand. If tails, search your deck for a Basic Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Flip a coin. If heads, search your deck for up to 2 Pokémon, reveal them, and put them into your hand. If tails, search your deck for a Basic Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.'),
)
