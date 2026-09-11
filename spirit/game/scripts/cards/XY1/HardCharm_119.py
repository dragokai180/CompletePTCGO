from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='19d26a1b-854f-50cb-a065-43287acb1299',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HardCharm.Name',
    display_name='Hard Charm',
    searchable_by=['Hard Charm', 'Pokémon Tool', 'HardCharm'],
    subtypes=['Pokémon Tool'],
    collector_number=119,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Any damage done to the Pokémon this card is attached to by an opponent's attack is reduced by 20 (after applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
