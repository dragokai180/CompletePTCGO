from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0a70b62e-2d2e-5903-8e07-025ef1f46eb8",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier","Stage 1","Escavalier"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard a Pokémon Tool card attached to the Defending Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Cavalry Lance",
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
