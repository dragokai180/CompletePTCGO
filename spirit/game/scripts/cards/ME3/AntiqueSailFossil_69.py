from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="ea6326a0-4192-5ef2-a996-423bd0e31cf7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSailFossil.Name",
    display_name="Antique Sail Fossil",
    searchable_by=["Antique Sail Fossil", "Item", "AntiqueSailFossil"],
    subtypes=["Item"],
    collector_number=69,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
