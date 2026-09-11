from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b6ab4528-d74c-5a38-a467-51d77467dece",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMabosstiffex.Name",
    display_name="Arven's Mabosstiff ex",
    searchable_by=["Arven's Mabosstiff ex", "Stage 1", "ex", "ArvensMabosstiffex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMaschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Vigorous Tackle",
            game_text="If this Pokémon has no damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Boss Headbutt",
            game_text="During your next turn, this Pokémon can't use Boss Headbutt.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
