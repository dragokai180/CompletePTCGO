from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="73caa7ea-127c-5c82-8f00-cc36aecb15c7",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile","Stage 2","Krookodile"],
    subtypes=["Stage 2"],
    collector_number=127,
    set_code="BW6",
    rarity=Rarities.RareSecret,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    abilities=[
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=dark_clamp,
        ),
        Attack(
            title="Bombast",
            game_text="Does 40 damage times the number of Prize cards you have taken.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
