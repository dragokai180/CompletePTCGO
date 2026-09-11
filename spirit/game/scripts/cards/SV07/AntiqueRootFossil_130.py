from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="4d2f3e05-3346-5374-a3c6-2f2c7effa7d5",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueRootFossil.Name",
    display_name="Antique Root Fossil",
    searchable_by=["Antique Root Fossil", "Item", "AntiqueRootFossil"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
