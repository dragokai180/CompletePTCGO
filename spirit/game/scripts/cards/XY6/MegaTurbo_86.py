from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='93d6b5c7-727b-5ba2-9c76-86b3b5e33917',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MegaTurbo.Name',
    display_name='Mega Turbo',
    searchable_by=['Mega Turbo', 'Item', 'MegaTurbo'],
    subtypes=['Item'],
    collector_number=86,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach a basic Energy card from your discard pile to 1 of your Mega Evolution Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Attach a basic Energy card from your discard pile to 1 of your Mega Evolution Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
