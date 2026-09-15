from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="da050c61-ae6a-568a-b7b6-6c02f99add87",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage","Stage 1","Simisage"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    abilities=[
        Attack(
            title="Fire's Power",
            game_text="If this Pokémon has any Fire Energy attached to it, the Defending Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
