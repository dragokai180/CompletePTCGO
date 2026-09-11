from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import hypnostrike, stellar_guidance
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6b699858-0eee-5a75-a45d-b9319e5bc6c6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel","Stage 1","Bibarel"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Tumbling Tackle",
            game_text="Both this Pokémon and the Defending Pokémon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=hypnostrike,
        ),
    ],
)
