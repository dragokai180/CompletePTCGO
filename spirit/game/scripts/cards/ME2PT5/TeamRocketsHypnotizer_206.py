from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="2209d1c7-ba86-550c-9d7d-9630ca3702a2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHypnotizer.Name",
    display_name="Team Rocket's Hypnotizer",
    searchable_by=["Team Rocket's Hypnotizer", "Pokémon Tool", "TeamRocketsHypnotizer"],
    subtypes=["Pokémon Tool"],
    collector_number=206,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Team Rocket's Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Team Rocket's Pokémon is Knocked Out), the Attacking Pokémon is now Asleep."),
)
