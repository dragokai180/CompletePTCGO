from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b083dacb-0e95-5a16-b847-f8dcc549d6f3',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonCirculator.Name',
    display_name='Pokémon Circulator',
    searchable_by=['Pokémon Circulator', 'Item', 'PokmonCirculator'],
    subtypes=['Item'],
    collector_number=81,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.'),
    condition=standard_trainer_condition('Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.'),
)
