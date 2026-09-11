from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f54a3999-16b8-5b65-abd8-76ea5df7846f',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AssaultVest.Name',
    display_name='Assault Vest',
    searchable_by=['Assault Vest', 'Pokémon Tool', 'AssaultVest'],
    subtypes=['Pokémon Tool'],
    collector_number=133,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Any damage done to the Pokémon this card is attached to by attacks from your opponent's Pokémon that have any Special Energy attached to them is reduced by 40 (after applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
