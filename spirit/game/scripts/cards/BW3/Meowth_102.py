from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import fury_swipes
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="daf64d51-e37f-52f2-b5d3-c1a80890627b",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth","Basic","Meowth"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="BW3",
    rarity=Rarities.RareSecret,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=fury_swipes,
        ),
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=draw_attack(1),
        ),
    ],
)
