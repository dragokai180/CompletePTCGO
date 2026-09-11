from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_bonus_attack
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def blazing_mane(ctx):
    """If this Pokémon is your Active Pokémon and is damaged by an opponent's
    attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is
    now Burned."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)



card = PokemonCardDef(
    guid="f04248f7-a04a-5720-bfba-cc97dbb50df4",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine","Stage 1","Arcanine"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    abilities=[
        Ability(
            title="Blazing Mane",
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=blazing_mane,
        ),
        Attack(
            title="Fire Spin",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
