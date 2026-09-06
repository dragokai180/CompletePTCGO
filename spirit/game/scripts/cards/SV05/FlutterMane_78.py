from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import (
    ability_lock_passive,
    is_in_active_spot,
    opposing_active,
)


def _midnight_fluttering_target(pokemon, carrier):
    return opposing_active(pokemon, carrier) and is_in_active_spot(carrier)


async def hex_hurl(ctx):
    """90. Put 2 damage counters on the opponent's Benched Pokemon in any
    way you like."""
    await ctx.deal_damage()
    await ctx.place_damage_counters(2, candidates=ctx.opponent_bench())


card = PokemonCardDef(
    guid="fc42f395-f296-5d84-9f93-816cdc92e660",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlutterMane.Name",
    display_name="Flutter Mane",
    searchable_by=["Flutter Mane", "Basic", "Ancient", "FlutterMane"],
    subtypes=["Basic", "Ancient"],
    collector_number=78,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=987,
    abilities=[
        Ability(
            title="Midnight Fluttering",
            game_text="As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon has no Abilities, except for Midnight Fluttering.",
            passive=ability_lock_passive(_midnight_fluttering_target),
        ),
        Attack(
            title="Hex Hurl",
            game_text="Put 2 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=hex_hurl,
        ),
    ],
)
