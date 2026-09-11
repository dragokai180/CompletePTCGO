from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='bcdf471d-5f95-5b66-9cc9-bcd7d0f57b00',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LuxuriousCape.Name',
    display_name='Luxurious Cape',
    searchable_by=['Luxurious Cape', 'Pokémon Tool', 'LuxuriousCape'],
    subtypes=['Pokémon Tool'],
    collector_number=166,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to doesn't have a Rule Box, it gets +100 HP, and if it is Knocked Out by damage from an attack from your opponent's Pokémon, that player takes 1 more Prize card. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"),
)
