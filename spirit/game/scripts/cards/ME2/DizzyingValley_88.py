from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="046a8a33-754f-551e-851e-f23043c5fe88",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DizzyingValley.Name",
    display_name="Dizzying Valley",
    searchable_by=["Dizzying Valley", "Stadium", "DizzyingValley"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Confused Pokémon (both yours and your opponent's) don't recover from that Special Condition when they evolve or devolve."),
    ability=standard_stadium_ability("Confused Pokémon (both yours and your opponent's) don't recover from that Special Condition when they evolve or devolve."),
)
