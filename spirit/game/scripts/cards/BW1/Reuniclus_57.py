from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import shadow_punch, sinister_hand, sinister_hand_condition
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2d173d0c-3394-5c28-b833-b743100a2301",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus","Stage 2","Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    abilities=[
        Ability(
            title="Damage Swap",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pokémon to another of your Pokémon.",
            activation=Activations.UNLIMITED,
            condition=sinister_hand_condition,
            effect=sinister_hand,
        ),
        Attack(
            title="Psywave",
            game_text="Does 10 more damage for each Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
