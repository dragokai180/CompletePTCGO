from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import CursedGlarePassive, blizzard
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e155c05a-7912-5014-8a62-4b63cd4c3029",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ExcadrillEX.Name",
    display_name="Excadrill-EX",
    searchable_by=["Excadrill-EX","Basic","EX","ExcadrillEX"],
    subtypes=["Basic","EX"],
    collector_number=82,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Dig Out",
            game_text="Discard the top card of your deck. If that card is a basic Energy card, attach it to 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Break Ground",
            game_text="Does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=blizzard,
        ),
    ],
)
