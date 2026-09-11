from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='790a9393-4d88-50ef-9dbe-0ce83805d7bd',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name',
    display_name='Great Catcher',
    searchable_by=['Great Catcher', 'Item', 'GreatCatcher'],
    subtypes=['Item'],
    collector_number=192,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if you discard 2 other cards from your hand. Switch 1 of your opponent's Benched Pokémon-GX or Pokémon-EX with their Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("You can play this card only if you discard 2 other cards from your hand. Switch 1 of your opponent's Benched Pokémon-GX or Pokémon-EX with their Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
