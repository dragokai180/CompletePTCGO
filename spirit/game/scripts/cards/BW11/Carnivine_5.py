from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="66c3933a-3ebc-5448-996a-ddd1718a1a51",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine","Basic","Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Ambush Bite",
            game_text="Flip a coin. If heads, this attack does 20 more damage and discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
