from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import retribution, signal_beam

card = PokemonCardDef(
    guid="77e8c458-a2ad-59c0-92d6-78f59415ed08",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasEX.Name",
    display_name="Latias-EX",
    searchable_by=["Latias-EX","Basic","EX","LatiasEX"],
    subtypes=["Basic","EX"],
    collector_number=85,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Ability(
            title="Bright Down",
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon with Abilities.",
            passive=bw_legacy_passive("Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon with Abilities."),
        ),
        Attack(
            title="Barrier Break",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
