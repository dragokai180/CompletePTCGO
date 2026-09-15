from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="c52e41f1-98ff-5256-a06e-e68b8b81c434",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant","Basic","Durant","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=91,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Hard Crunch",
            game_text="If the Defending Pokémon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
