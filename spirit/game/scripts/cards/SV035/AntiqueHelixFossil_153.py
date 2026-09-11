from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = FossilItemCardDef(
    guid='b500d3cb-ce10-5632-a8aa-325059584f49',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AntiqueHelixFossil.Name',
    display_name='Antique Helix Fossil',
    searchable_by=['Antique Helix Fossil', 'Item', 'AntiqueHelixFossil'],
    subtypes=['Item'],
    collector_number=153,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
