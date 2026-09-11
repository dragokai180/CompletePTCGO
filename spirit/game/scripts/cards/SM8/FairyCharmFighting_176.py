from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='d593bdd3-d911-5f18-a563-8b982abb51e9',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmFighting.Name',
    display_name='Fairy Charm Fighting',
    searchable_by=['Fairy Charm Fighting', 'Pokémon Tool', 'FairyCharmFighting'],
    subtypes=['Pokémon Tool'],
    collector_number=176,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Fighting Pokémon-GX and Fighting Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
