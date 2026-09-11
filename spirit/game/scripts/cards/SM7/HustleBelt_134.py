from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='49e3b91b-b484-5d93-947b-c98ce10f2026',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name',
    display_name='Hustle Belt',
    searchable_by=['Hustle Belt', 'Pokémon Tool', 'HustleBelt'],
    subtypes=['Pokémon Tool'],
    collector_number=134,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to has 30 HP or less remaining and has any damage counters on it, its attacks do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
