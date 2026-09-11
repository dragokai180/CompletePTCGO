from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='c5db833a-f6e7-5921-bb4f-e42d5ad70b6c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProtectiveGoggles.Name',
    display_name='Protective Goggles',
    searchable_by=['Protective Goggles', 'Pokémon Tool', 'ProtectiveGoggles'],
    subtypes=['Pokémon Tool'],
    collector_number=164,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Basic Pokémon this card is attached to has no Weakness.'),
)
