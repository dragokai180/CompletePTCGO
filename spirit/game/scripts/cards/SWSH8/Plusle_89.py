from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


from spirit.game.card_effects.attacks_common import previous_attack_matches


def _minun_attacked_last_turn(ctx):
    return previous_attack_matches(ctx.board, ctx.player_id, name="Minun")


card = PokemonCardDef(
    guid="09d414a6-492a-5dc7-84b1-f72d403d8b26",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Rapid Strike", "Plusle"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=89,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=311,
    abilities=[
        Attack(
            title="Spark Duo",
            game_text="If 1 of your Minun used an attack during your last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_minun_attacked_last_turn, 100),
        ),
    ],
)
