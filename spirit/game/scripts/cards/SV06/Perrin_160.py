from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="7cc10ee0-6a32-5930-845a-114b5e224f7c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Perrin.Name",
    display_name="Perrin",
    searchable_by=["Perrin", "Supporter", "Perrin"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Reveal up to 2 Pokémon in your hand and put them into your deck. If you do, search your deck for up to that many Pokémon, reveal them, and put them into your hand. Then, shuffle your deck."),
)
