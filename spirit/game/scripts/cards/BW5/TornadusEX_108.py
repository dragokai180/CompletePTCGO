from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="a37651ba-321f-57b7-85dc-f88842e59a4f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusEX.Name",
    display_name="Tornadus-EX",
    searchable_by=["Tornadus-EX","Basic","EX","TornadusEX"],
    subtypes=["Basic","EX"],
    collector_number=108,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If there is any Stadium card in play, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Power Blast",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
