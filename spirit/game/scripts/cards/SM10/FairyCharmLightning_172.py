from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='bf0cb66a-2a98-516e-b038-bd443a6bfa7c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmLightning.Name',
    display_name='Fairy Charm Lightning',
    searchable_by=['Fairy Charm Lightning', 'Pokémon Tool', 'FairyCharmLightning'],
    subtypes=['Pokémon Tool'],
    collector_number=172,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Lightning Pokémon-GX and Lightning Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
