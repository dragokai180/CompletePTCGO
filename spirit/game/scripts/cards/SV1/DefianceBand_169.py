from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='569fe763-9226-5205-8e9c-a50b6104208f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DefianceBand.Name',
    display_name='Defiance Band',
    searchable_by=['Defiance Band', 'Pokémon Tool', 'DefianceBand'],
    subtypes=['Pokémon Tool'],
    collector_number=169,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("If you have more Prize cards remaining than your opponent, the attacks of the Pokémon this card is attached to do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
