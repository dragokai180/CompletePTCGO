from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, flip_damage, lock_all_attacks
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.session.legal_actions import energy_provided_count

async def freeze_shock(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)




card = PokemonCardDef(
    guid="538c6b3c-b2e0-585d-9f6f-3fa60a61aa63",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremEX.Name",
    display_name="Black Kyurem-EX",
    searchable_by=["Black Kyurem-EX","Basic","EX","BlackKyuremEX"],
    subtypes=["Basic","EX"],
    collector_number=100,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Dragon Fang",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Freeze Shock",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=freeze_shock,
        ),
    ],
)
