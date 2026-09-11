from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='ca356f20-8348-56dc-8aa3-f650d36c0f43',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BentSpoon.Name',
    display_name='Bent Spoon',
    searchable_by=['Bent Spoon', 'Pokémon Tool', 'BentSpoon'],
    subtypes=['Pokémon Tool'],
    collector_number=93,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to the Pokémon this card is attached to. (Existing effects are not removed.) You may play as many Item cards as you like during your turn (before your attack)."),
)
