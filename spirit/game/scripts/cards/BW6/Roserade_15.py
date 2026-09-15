from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="79ff3208-3405-5b91-88a0-199c89f07d21",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade","Stage 1","Roserade"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    abilities=[
        Ability(
            title="Le Parfum",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may search your deck for any card and put it into your hand. Shuffle your deck afterward.",
            trigger="on_evolve",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
