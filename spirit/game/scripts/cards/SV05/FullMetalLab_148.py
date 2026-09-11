from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="40604de2-33bc-557c-bcbc-b23665cbb5e8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullMetalLab.Name",
    display_name="Full Metal Lab",
    searchable_by=["Full Metal Lab", "Stadium", "FullMetalLab"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Metal Pokémon (both yours and your opponent's) take 30 less damage from attacks from the opponent's Pokémon (after applying Weakness and Resistance)."),
    ability=standard_stadium_ability("Metal Pokémon (both yours and your opponent's) take 30 less damage from attacks from the opponent's Pokémon (after applying Weakness and Resistance)."),
)
