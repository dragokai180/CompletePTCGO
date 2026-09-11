from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2b1e8ed9-df4a-57d5-b991-0dd7af8723f0",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino","Stage 1","Cinccino"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    abilities=[
        Ability(
            title="Smooth Coat",
            game_text="If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Smooth Coat"),
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=bw_legacy_attack,
        ),
    ],
)
