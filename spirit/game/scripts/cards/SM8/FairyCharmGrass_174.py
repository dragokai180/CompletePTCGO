from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='aea91199-90d4-5f3c-8319-74276b621455',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmGrass.Name',
    display_name='Fairy Charm Grass',
    searchable_by=['Fairy Charm Grass', 'Pokémon Tool', 'FairyCharmGrass'],
    subtypes=['Pokémon Tool'],
    collector_number=174,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Grass Pokémon-GX and Grass Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
