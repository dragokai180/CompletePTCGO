from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="44b739e6-dd45-5375-9e2d-7862c8860f12",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeloettaEX.Name",
    display_name="Meloetta-EX",
    searchable_by=["Meloetta-EX","Basic","EX","MeloettaEX"],
    subtypes=["Basic","EX"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=126,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC11"}},
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Brilliant Voice",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Asleep. If tails, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Round",
            game_text="Does 30 damage times the number of your Pokémon that have the Round attack.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
