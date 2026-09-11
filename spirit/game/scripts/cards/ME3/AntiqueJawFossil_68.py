from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="fa34c662-3f2c-513c-b977-69f0dbad66e4",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueJawFossil.Name",
    display_name="Antique Jaw Fossil",
    searchable_by=["Antique Jaw Fossil", "Item", "AntiqueJawFossil"],
    subtypes=["Item"],
    collector_number=68,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
