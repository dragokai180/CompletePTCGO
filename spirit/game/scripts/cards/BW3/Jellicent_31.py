from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_bonus_attack
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def cursed_body(ctx):
    """If this Pokémon is your Active Pokémon and is damaged by an opponent's
    attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is
    now Confused."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)



card = PokemonCardDef(
    guid="4a473049-803a-50f5-9c67-71fbb5489724",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent","Stage 1","Jellicent"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    abilities=[
        Ability(
            title="Cursed Body",
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Confused.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=cursed_body,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
