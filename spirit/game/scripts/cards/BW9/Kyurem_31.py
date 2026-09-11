from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, lock_all_attacks
from spirit.game.session.legal_actions import energy_provided_count
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def blizzard_burn(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)



card = PokemonCardDef(
    guid="843ca95c-7152-5a4b-82fc-071feb359570",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem","Basic","Kyurem"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Frost Spear",
            game_text="Does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=blizzard_burn,
        ),
    ],
)
