from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='bdfab0b2-e405-5f82-9a79-2dcf3987e2ed',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name',
    display_name='Max Revive',
    searchable_by=['Max Revive', 'Item', 'MaxRevive'],
    subtypes=['Item'],
    collector_number=120,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put a Pokémon from your discard pile on top of your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put a Pokémon from your discard pile on top of your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
