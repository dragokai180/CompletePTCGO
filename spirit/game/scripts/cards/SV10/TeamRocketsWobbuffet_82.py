from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


async def rocket_mirror(ctx):
    """Move all damage counters from 1 of your Benched Team Rocket's Pokémon
    to your opponent's Active Pokémon."""
    candidates = [
        p for p in ctx.my_bench()
        if _is_team_rockets(p)
        and ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0) > 0
    ]
    if not candidates:
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose your Benched Team Rocket's Pokémon"
    )
    dest = ctx.opponent_active()
    if source is None or dest is None:
        return
    await ctx.move_damage_counters(source, dest)


card = PokemonCardDef(
    guid="0cb7d35b-cb72-5e86-94b9-09c0b2e6ba81",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsWobbuffet.Name",
    display_name="Team Rocket's Wobbuffet",
    searchable_by=["Team Rocket's Wobbuffet", "Basic", "TeamRocketsWobbuffet"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=202,
    abilities=[
        Attack(
            title="Rocket Mirror",
            game_text="Move all damage counters from 1 of your Benched Team Rocket's Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=rocket_mirror,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
