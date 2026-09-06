from spirit.game.data_utils import EnergyCardDef, def_for
from spirit.game.attributes import PokemonTypes, Rarities


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


card = EnergyCardDef(
    guid="94bd80de-a4be-5a50-8ecf-0787d5c67b3c",
    key="SV10",
    name="Team Rocket's Energy",
    display_name="Team Rocket's Energy",
    searchable_by=["Team Rocket's Energy", "Special", "TeamRocketsEnergy"],
    subtypes=["Special"],
    collector_number=182,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=_is_team_rockets,
    discard_if_invalid=True,
    provides=[
        [PokemonTypes.PSYCHIC, PokemonTypes.PSYCHIC],
        [PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS],
        [PokemonTypes.DARKNESS, PokemonTypes.DARKNESS],
    ],
)
