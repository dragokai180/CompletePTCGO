from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy


async def power_rush(ctx):
    """200. Flip a coin. If tails, during your next turn, this Pokémon
    can't use attacks."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Power Rush"))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e3ed14ae-2b32-53cf-8b0e-9790525f646f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikouex.Name",
    display_name="Raikou ex",
    searchable_by=["Raikou ex","Basic","ex","Raikouex"],
    subtypes=["Basic","ex"],
    collector_number=24,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Lightning Cloak",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for a Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            usable_first_turn=True,
            effect=search_attach_energy(
                predicate=is_lightning_energy, count=1, to_self=True,
            ),
        ),
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=power_rush,
        ),
    ],
)
