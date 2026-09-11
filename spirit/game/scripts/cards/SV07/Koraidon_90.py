from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bfbd60cc-c58f-5f05-9a63-685319248c41",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Koraidon"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Resolute Fang",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
