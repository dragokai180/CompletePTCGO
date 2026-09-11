from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0931dfc6-ca6e-52de-9de9-8d80ba7d13d1",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales","Stage 1","Ninetales"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    abilities=[
        Ability(
            title="Bright Look",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.",
            trigger="on_evolve",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Hexed Flame",
            game_text="Does 50 more damage for each Special Condition affecting the Defending Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
