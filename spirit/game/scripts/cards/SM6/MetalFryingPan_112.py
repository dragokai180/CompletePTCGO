from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='52b2b3ca-fdbd-5761-874f-87ec4c16bcf2',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MetalFryingPan.Name',
    display_name='Metal Frying Pan',
    searchable_by=['Metal Frying Pan', 'Pokémon Tool', 'MetalFryingPan'],
    subtypes=['Pokémon Tool'],
    collector_number=112,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Metal Pokémon this card is attached to takes 30 less damage from your opponent's attacks (after applying Weakness and Resistance) and has no Weakness. You may play as many Item cards as you like during your turn (before your attack)."),
)
