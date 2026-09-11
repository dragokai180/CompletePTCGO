from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="49e9f325-fd73-5c8a-8de6-f32ae43b9277",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo","Basic","Tynamo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, attach an Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=bw_legacy_attack,
        ),
    ],
)
