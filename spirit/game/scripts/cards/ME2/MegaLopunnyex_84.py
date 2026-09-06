from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, ignore_effects_attack


def _entered_active_this_turn(ctx):
    return ctx.entered_active_this_turn(ctx.attacker)


card = PokemonCardDef(
    guid="e009a083-752e-5d5d-b812-a0f43fdd8bad",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyex.Name",
    display_name="Mega Lopunny ex",
    searchable_by=["Mega Lopunny ex", "Stage 1", "ex", "SV_Mega", "MegaLopunnyex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=84,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 170 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_entered_active_this_turn, 170),
        ),
        Attack(
            title="Spiky Hopper",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=ignore_effects_attack(),
        ),
    ],
)
