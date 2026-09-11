from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='b3138bdc-662a-53b3-b63f-dbf4ab9d0414',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Beastite.Name',
    display_name='Beastite',
    searchable_by=['Beastite', 'Pokémon Tool', 'Beastite'],
    subtypes=['Pokémon Tool'],
    collector_number=185,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of the Ultra Beast this card is attached to do 10 more damage to your opponent's Active Pokémon for each Prize card you have taken (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
