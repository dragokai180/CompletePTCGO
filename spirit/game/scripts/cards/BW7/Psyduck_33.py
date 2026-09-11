from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="b6e34221-da09-5b1d-87ef-6891ab236b10",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck","Basic","Psyduck"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Firefighting",
            game_text="Discard a Fire Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
