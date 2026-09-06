from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import bonus_if, flip_damage


def _played_team_rocket_supporter(ctx):
    return ctx.played_trainer_this_turn(
        lambda r: r[2] == TrainerType.SUPPORTER.value and "Team Rocket" in r[1]
    ) > 0


card = PokemonCardDef(
    guid="b26593f5-bc6f-51ed-b5f1-50d5a5416da2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKangaskhanex.Name",
    display_name="Team Rocket's Kangaskhan ex",
    searchable_by=["Team Rocket's Kangaskhan ex","Basic","ex","TeamRocketsKangaskhanex"],
    subtypes=["Basic","ex"],
    collector_number=162,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    family_id=115,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=30),
        ),
        Attack(
            title="Wicked Impact",
            game_text="If you played a Supporter card that has \"Team Rocket\" in its name from your hand during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_played_team_rocket_supporter, 100),
        ),
    ],
)
