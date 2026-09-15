from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="8615af42-d009-50c3-9a47-11ad919be95b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor","Stage 2","Staraptor"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Strong Breeze",
            game_text="Your opponent shuffles the Defending Pokémon and all cards attached to it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=bw_legacy_attack,
        ),
    ],
)
