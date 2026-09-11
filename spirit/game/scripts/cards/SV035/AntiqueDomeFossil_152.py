from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = FossilItemCardDef(
    guid='7a9a3cf8-041b-53a4-b40f-57efa201c75c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AntiqueDomeFossil.Name',
    display_name='Antique Dome Fossil',
    searchable_by=['Antique Dome Fossil', 'Item', 'AntiqueDomeFossil'],
    subtypes=['Item'],
    collector_number=152,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
