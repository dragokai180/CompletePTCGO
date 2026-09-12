from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="bb81a3a3-2a8e-58ba-a211-068fbbfa1ee7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX","Basic","EX","ThundurusEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=110,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Raiden Knuckle",
            game_text="Attach an Energy card from your discard pile to 1 of your Benched Team Plasma Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Thunderous Noise",
            game_text="If this Pokémon has any Plasma Energy attached to it, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)
