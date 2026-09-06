from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


async def team_rockets_ariana(ctx):
    """Draw until 5, or until 8 if all your Pokémon in play are Team Rocket's."""
    in_play = ctx.my_pokemon_in_play()
    target = 8 if in_play and all(_is_team_rockets(p) for p in in_play) else 5
    await ctx.draw_until(target)


card = SupporterCardDef(
    guid="acc9eb19-26eb-5c64-a744-34c8b3cb3607",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsAriana.Name",
    display_name="Team Rocket's Ariana",
    searchable_by=["Team Rocket's Ariana", "Supporter", "TeamRocketsAriana"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=team_rockets_ariana,
)
