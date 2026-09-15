from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import destructive_beam
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="bcb8fcca-4e78-5119-8418-1276a2d53500",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresEX.Name",
    display_name="Moltres-EX",
    searchable_by=["Moltres-EX","Basic","EX","MoltresEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=14,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Destructive Flame",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=destructive_beam,
        ),
        Attack(
            title="Power Flame",
            game_text="If this Pokémon has any Plasma Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
