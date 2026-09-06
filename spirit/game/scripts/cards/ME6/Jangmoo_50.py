from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive

async def hard_head(ctx):
    """30. During your opponent's next turn, this Pokémon takes 30 less damage
    from attacks (after applying Weakness and Resistance) ."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(30))

card = PokemonCardDef(
    guid="c41a1911-1cd2-57cf-b69e-f3cce4a238c7",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    display_name="Jangmo-o",
    searchable_by=["Jangmo-o","Basic","Jangmoo"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=782,
    abilities=[
        Attack(
            title="Hard Head",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance) .",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=hard_head,
        ),
    ],
)
