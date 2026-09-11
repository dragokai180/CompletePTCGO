from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='8067bf07-1cd5-588d-b3b2-dfd6ab99c2ff',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyPouch.Name',
    display_name='Energy Pouch',
    searchable_by=['Energy Pouch', 'Pokémon Tool', 'EnergyPouch'],
    subtypes=['Pokémon Tool'],
    collector_number=97,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put all basic Energy attached to that Pokémon into your hand. You may play as many Item cards as you like during your turn (before your attack)."),
)
