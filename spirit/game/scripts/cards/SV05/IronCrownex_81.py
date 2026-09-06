from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for, subtypes_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _cobalt_attacker(pokemon):
    if "Future" not in subtypes_for(pokemon.archetype_id):
        return False
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name != "Iron Crown ex"


async def twin_shotels(ctx):
    """50 damage to 2 of the opponent's Pokémon; ignore W/R and effects."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    count = min(2, len(candidates))
    picks = await ctx.choose_cards(
        candidates, count,
        prompt="Choose 2 of your opponent's Pokémon to take 50 damage",
    )
    for target in picks:
        await ctx.deal_damage(
            50, target=target, apply_modifiers=False, ignore_target_effects=True,
        )


card = PokemonCardDef(
    guid="cc0b9952-499a-57fc-9ac5-ea21e7cd9cbf",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronCrownex.Name",
    display_name="Iron Crown ex",
    searchable_by=["Iron Crown ex","Basic","ex","Future","IronCrownex"],
    subtypes=["Basic","ex","Future"],
    collector_number=81,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=1023,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Cobalt Command",
            game_text="Attacks used by your Future Pokémon, except any Iron Crown ex, do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=_cobalt_attacker),
        ),
        Attack(
            title="Twin Shotels",
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance, or by any effects on those Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=twin_shotels,
        ),
    ],
)
