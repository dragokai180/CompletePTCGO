from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="dc9260f8-a956-57ba-af3f-c66444f692f1",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo","Stage 2","Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    abilities=[
        Ability(
            title="Rain Dish",
            game_text="At any times between turns, heal 20 damage from this Pokémon.",
            trigger="between_turns",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Groovy Dance",
            game_text="You may discard an Energy attached to this Pokémon. If you do, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
