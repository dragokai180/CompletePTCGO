from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_bonus_attack
from spirit.game.card_effects.pokemon import in_active_spot

async def poison_point(ctx):
    """If this Pokémon is your Active Pokémon and is damaged by an opponent's
    attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is
    now Poisoned."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)



card = PokemonCardDef(
    guid="9e906f62-7af8-5024-b2f0-153b9bf09daf",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    display_name="Venipede",
    searchable_by=["Venipede","Basic","Venipede"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=poison_point,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
