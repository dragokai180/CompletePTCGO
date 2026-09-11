from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='6c240695-897c-5aab-8df8-f67f879df73b',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.StartlingMegaphone.Name',
    display_name='Startling Megaphone',
    searchable_by=['Startling Megaphone', 'Item', 'StartlingMegaphone'],
    subtypes=['Item'],
    collector_number=97,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard all Pokémon Tool cards attached to each of your opponent's Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Discard all Pokémon Tool cards attached to each of your opponent's Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
