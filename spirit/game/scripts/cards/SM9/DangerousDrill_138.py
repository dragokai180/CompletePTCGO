from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='d1f44010-4fbc-5195-be78-de8b65fb1949',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name',
    display_name='Dangerous Drill',
    searchable_by=['Dangerous Drill', 'Item', 'DangerousDrill'],
    subtypes=['Item'],
    collector_number=138,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if you discard a Darkness Pokémon from your hand. Discard a Pokémon Tool or Special Energy card from 1 of your opponent's Pokémon, or discard any Stadium card in play. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("You can play this card only if you discard a Darkness Pokémon from your hand. Discard a Pokémon Tool or Special Energy card from 1 of your opponent's Pokémon, or discard any Stadium card in play. You may play as many Item cards as you like during your turn (before your attack)."),
)
