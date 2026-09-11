from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='aa83f6fc-449f-5100-9633-a1ff5d59271f',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FocusSash.Name',
    display_name='Focus Sash',
    searchable_by=['Focus Sash', 'Pokémon Tool', 'FocusSash'],
    subtypes=['Pokémon Tool'],
    collector_number=91,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Fighting Pokémon this card is attached to has full HP and would be Knocked Out by damage from an opponent's attack, that Pokémon is not Knocked Out and its remaining HP becomes 10 instead. Then, discard this card. You may play as many Item cards as you like during your turn (before your attack)."),
)
