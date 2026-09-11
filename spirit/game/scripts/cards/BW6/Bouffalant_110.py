from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="5b93cdfa-e7a7-51ba-95f9-78eaba1ad62d",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant","Basic","Bouffalant"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            passive=bw_legacy_passive("Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title="Gold Breaker",
            game_text="If the Defending Pokémon is a Pokémon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
