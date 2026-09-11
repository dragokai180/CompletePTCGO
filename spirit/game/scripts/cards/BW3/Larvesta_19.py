from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="17378d78-4b62-5837-be95-6fbc4f79992b",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta","Basic","Larvesta"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
    ],
)
