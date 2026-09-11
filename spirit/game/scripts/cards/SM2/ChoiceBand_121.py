from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='153670d3-a44c-5c04-a706-4d49d0df9153',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name',
    display_name='Choice Band',
    searchable_by=['Choice Band', 'Pokémon Tool', 'ChoiceBand'],
    subtypes=['Pokémon Tool'],
    collector_number=121,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of the Pokémon this card is attached to do 30 more damage to your opponent's Active Pokémon-GX or Active Pokémon-EX (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
