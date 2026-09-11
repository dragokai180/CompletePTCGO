from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='57d7e7f5-52e6-5255-af70-62d8d97943eb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name',
    display_name='Metal Goggles',
    searchable_by=['Metal Goggles', 'Pokémon Tool', 'MetalGoggles'],
    subtypes=['Pokémon Tool'],
    collector_number=148,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Metal Pokémon this card is attached to takes 30 less damage from your opponent's attacks (after applying Weakness and Resistance), and your opponent's attacks and Abilities can't put damage counters on it. You may play as many Item cards as you like during your turn (before your attack)."),
)
