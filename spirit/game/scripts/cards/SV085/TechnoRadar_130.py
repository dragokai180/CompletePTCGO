from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="53189343-e9df-5abb-a357-72830da5532b",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnoRadar.Name",
    display_name="Techno Radar",
    searchable_by=["Techno Radar", "Item", "Future", "TechnoRadar"],
    subtypes=["Item", "Future"],
    collector_number=130,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you discard another card from your hand.  Search your deck for up to 2 Future Pokémon, reveal them, and put them into your hand. Then, shuffle your deck."),
)
