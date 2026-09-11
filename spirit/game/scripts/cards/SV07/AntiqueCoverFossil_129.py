from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="776f60a3-b390-5f43-a75b-742e47f8aed9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    display_name="Antique Cover Fossil",
    searchable_by=["Antique Cover Fossil", "Item", "AntiqueCoverFossil"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.    At any time during your turn, you may discard this card from play."),
)
