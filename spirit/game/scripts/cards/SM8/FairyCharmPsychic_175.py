from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='25618b26-4e48-57ab-b132-9df0db13e5a7',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmPsychic.Name',
    display_name='Fairy Charm Psychic',
    searchable_by=['Fairy Charm Psychic', 'Pokémon Tool', 'FairyCharmPsychic'],
    subtypes=['Pokémon Tool'],
    collector_number=175,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Psychic Pokémon-GX and Psychic Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
