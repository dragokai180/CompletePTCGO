from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="d7c7fd29-8a46-51c4-8132-5d3334ed7de7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiquePlumeFossil.Name",
    display_name="Antique Plume Fossil",
    searchable_by=["Antique Plume Fossil", "Item", "AntiquePlumeFossil"],
    subtypes=["Item"],
    collector_number=79,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.  At any time during your turn, you may discard this card from play."),
)
