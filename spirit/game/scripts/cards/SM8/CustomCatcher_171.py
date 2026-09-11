from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5a24ef95-4cb6-54f6-bc94-febcd8d2dc2b',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CustomCatcher.Name',
    display_name='Custom Catcher',
    searchable_by=['Custom Catcher', 'Item', 'CustomCatcher'],
    subtypes=['Item'],
    collector_number=171,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You may play 2 Custom Catcher cards at once.\n• If you played 1 card, draw cards until you have 3 cards in your hand.\n• If you played 2 cards, switch 1 of your opponent's Benched Pokémon with their Active Pokémon. (This effects works one time for 2 cards.) You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("You may play 2 Custom Catcher cards at once.\n• If you played 1 card, draw cards until you have 3 cards in your hand.\n• If you played 2 cards, switch 1 of your opponent's Benched Pokémon with their Active Pokémon. (This effects works one time for 2 cards.) You may play as many Item cards as you like during your turn (before your attack)."),
)
