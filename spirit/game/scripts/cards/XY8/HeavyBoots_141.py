from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='45cfde93-0bea-5428-b2b2-cc8af213e333',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HeavyBoots.Name',
    display_name='Heavy Boots',
    searchable_by=['Heavy Boots', 'Pokémon Tool', 'HeavyBoots'],
    subtypes=['Pokémon Tool'],
    collector_number=141,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Retreat Cost of the Pokémon this card is attached to is 3 or more, that Pokémon gets +20 HP and can't be Confused. (If that Pokémon is currently Confused, remove that Special Condition.) You may play as many Item cards as you like during your turn (before your attack)."),
)
