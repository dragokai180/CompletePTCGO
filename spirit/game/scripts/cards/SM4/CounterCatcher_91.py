from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ddc7dd43-0e60-5821-bf9d-f0f65e848a70',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name',
    display_name='Counter Catcher',
    searchable_by=['Counter Catcher', 'Item', 'CounterCatcher'],
    subtypes=['Item'],
    collector_number=91,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if you have more Prize cards remaining than your opponent. Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("You can play this card only if you have more Prize cards remaining than your opponent. Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
