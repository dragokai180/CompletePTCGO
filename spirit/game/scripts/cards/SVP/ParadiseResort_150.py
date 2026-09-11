from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="482c957e-2f65-50de-9818-40fdfe298843",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParadiseResort.Name",
    display_name="Paradise Resort",
    searchable_by=["Paradise Resort", "Stadium", "ParadiseResort"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    passive=standard_passive("The Retreat Cost of each Psyduck in play (both yours and your opponent's) is Colorless less."),
    ability=standard_stadium_ability("The Retreat Cost of each Psyduck in play (both yours and your opponent's) is Colorless less."),
)
