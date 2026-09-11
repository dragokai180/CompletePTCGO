from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="b03c5a33-0505-54d0-abbd-8d0286554575",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysVitality.Name",
    display_name="Misty's Vitality",
    searchable_by=["Misty's Vitality", "Supporter", "MistysVitality"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for up to 4 Basic Water Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. Your turn ends."),
)
