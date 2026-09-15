from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import hide
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="84bf6828-6a14-513b-9a6e-f2576cdaa22a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZapdosEX.Name",
    display_name="Zapdos-EX",
    searchable_by=["Zapdos-EX","Basic","EX","ZapdosEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=48,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=hide,
        ),
        Attack(
            title="Powervolt",
            game_text="If this Pokémon has any Plasma Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
