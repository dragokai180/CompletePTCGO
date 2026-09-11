from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='69cc2e46-9d61-5ccf-8927-f5264056f8c5',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmUB.Name',
    display_name='Fairy Charm UB',
    searchable_by=['Fairy Charm UB', 'Pokémon Tool', 'FairyCharmUB'],
    subtypes=['Pokémon Tool'],
    collector_number=142,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Ultra Beast Pokémon-GX and Ultra Beast Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
