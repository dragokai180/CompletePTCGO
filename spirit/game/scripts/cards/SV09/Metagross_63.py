from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="251bade1-c689-5d5d-b94c-25358ed83407",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=63,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
        ),
        Attack(
            title="Conjoined Beams",
            game_text="If Beldum and Metang are on your Bench, this attack does 150 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
