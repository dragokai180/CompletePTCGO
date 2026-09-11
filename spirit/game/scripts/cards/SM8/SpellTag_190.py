from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='defcd8b2-4da8-5767-866c-cee06b007692',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SpellTag.Name',
    display_name='Spell Tag',
    searchable_by=['Spell Tag', 'Pokémon Tool', 'SpellTag'],
    subtypes=['Pokémon Tool'],
    collector_number=190,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("When the Psychic Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pokémon in any way you like. You may play as many Item cards as you like during your turn (before your attack)."),
)
