from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="601ba66f-41b2-5a8d-8aee-8c5b55714810",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PerilousJungle.Name",
    display_name="Perilous Jungle",
    searchable_by=["Perilous Jungle", "Stadium", "PerilousJungle"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("During Pokémon Checkup, put 2 more damage counters on each Poisoned non-Darkness Pokémon (both yours and your opponent's)."),
    ability=standard_stadium_ability("During Pokémon Checkup, put 2 more damage counters on each Poisoned non-Darkness Pokémon (both yours and your opponent's)."),
)
