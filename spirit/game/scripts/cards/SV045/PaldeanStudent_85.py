from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9442ddba-0723-53bb-91d6-77bd4d8c4e5b',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PaldeanStudent.Name',
    display_name='Paldean Student',
    searchable_by=['Paldean Student', 'Supporter', 'PaldeanStudent'],
    subtypes=['Supporter'],
    collector_number=85,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Search your deck for a Pokémon that doesn't have a Rule Box, reveal it, and put it into your hand. For each Paldean Student card (not including this card) in your discard pile, you may search for an additional Pokémon in this way. Then, shuffle your deck. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"),
    condition=standard_trainer_condition("Search your deck for a Pokémon that doesn't have a Rule Box, reveal it, and put it into your hand. For each Paldean Student card (not including this card) in your discard pile, you may search for an additional Pokémon in this way. Then, shuffle your deck. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"),
)
