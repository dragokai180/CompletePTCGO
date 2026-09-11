from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = FossilItemCardDef(
    guid="a46e2788-672b-515f-838e-296ebce9f735",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSkullFossil.Name",
    display_name="Antique Skull Fossil",
    searchable_by=["Antique Skull Fossil", "Item", "AntiqueSkullFossil"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=standard_passive("Play this card as if it were a 60-HP Basic Colorless Pokémon. This card can't be affected by any Special Conditions and can't retreat.\n \nAt any time during your turn, you may discard this card from play."),
)
