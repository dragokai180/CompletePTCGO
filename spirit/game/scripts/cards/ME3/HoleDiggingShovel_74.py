from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="f2157432-6c82-5d4d-8240-bd1fdc2851b6",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HoleDiggingShovel.Name",
    display_name="Hole-Digging Shovel",
    searchable_by=["Hole-Digging Shovel", "Item", "HoleDiggingShovel"],
    subtypes=["Item"],
    collector_number=74,
    set_code="ME3",
    regulation_mark="I",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Discard the top 2 cards of your deck."),
)
