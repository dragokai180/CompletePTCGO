from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="361af889-194a-5182-91ca-9f45b2bd91dc",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill","Stage 1","Excadrill"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Drill Run",
            game_text="Discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
