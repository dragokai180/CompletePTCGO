from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='81b11637-88ca-5d85-8101-26390a2fb766',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EcoArm.Name',
    display_name='Eco Arm',
    searchable_by=['Eco Arm', 'Item', 'EcoArm'],
    subtypes=['Item'],
    collector_number=71,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle 3 Pokémon Tool cards from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Shuffle 3 Pokémon Tool cards from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
