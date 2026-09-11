from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import giga_frost, outrage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="010334b7-ea33-5ba5-977c-11d6a01f2eef",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasEX.Name",
    display_name="Regigigas-EX",
    searchable_by=["Regigigas-EX","Basic","EX","RegigigasEX"],
    subtypes=["Basic","EX"],
    collector_number=82,
    set_code="BW4",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Giga Power",
            game_text="You may do 20 more damage. If you do, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Raging Hammer",
            game_text="Does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=outrage,
        ),
    ],
)
