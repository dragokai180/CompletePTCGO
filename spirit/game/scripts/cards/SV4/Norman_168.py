from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f35175d6-7f35-5101-8b34-fc7ae1a23b92',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Norman.Name',
    display_name='Norman',
    searchable_by=['Norman', 'Supporter', 'Norman'],
    subtypes=['Supporter'],
    collector_number=168,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 2 cards. If your opponent's Active Pokémon is a Pokémon ex, draw 2 more cards."),
    condition=standard_trainer_condition("Draw 2 cards. If your opponent's Active Pokémon is a Pokémon ex, draw 2 more cards."),
)
