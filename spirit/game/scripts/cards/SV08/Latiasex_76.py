from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.effects import is_basic_pokemon


async def eon_blade(ctx):
    """200. During your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="fa1a899f-b514-5fa2-a9c8-3bd966b0d3fd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiasex.Name",
    display_name="Latias ex",
    searchable_by=["Latias ex", "Basic", "ex", "Latiasex"],
    subtypes=["Basic", "ex"],
    collector_number=76,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=380,
    abilities=[
        Ability(
            title="Skyliner",
            game_text="Your Basic Pokémon in play have no Retreat Cost.",
            passive=retreat_free_when(
                lambda p, c: (
                    p.owning_player_id == c.owning_player_id
                    and is_basic_pokemon(p)
                ),
            ),
        ),
        Attack(
            title="Eon Blade",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=eon_blade,
        ),
    ],
)
