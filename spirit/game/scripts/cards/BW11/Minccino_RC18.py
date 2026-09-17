from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="1cc5de26-9302-55ac-bc20-61807dcecdff",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino","Basic","Minccino"],
    subtypes=["Basic"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=133,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC18"}},
    set_code="BW11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Tail Slap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)
