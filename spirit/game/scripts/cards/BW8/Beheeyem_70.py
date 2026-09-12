from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="b901b866-2d57-54a0-8198-e651bab1bd51",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem","Stage 1","Beheeyem","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=70,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    abilities=[
        Attack(
            title="Lock Up",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=dark_clamp,
        ),
        Attack(
            title="Damakinesis",
            game_text="Move 6 damage counters from any of your Pokémon to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=bw_legacy_attack,
        ),
    ],
)
