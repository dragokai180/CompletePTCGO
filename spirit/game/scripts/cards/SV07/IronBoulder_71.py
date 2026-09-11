from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="18bce158-fce3-52f4-917d-be782d98b6a6",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulder.Name",
    display_name="Iron Boulder",
    searchable_by=["Iron Boulder", "Basic", "Future", "IronBoulder"],
    subtypes=["Basic", "Future"],
    collector_number=71,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=1022,
    abilities=[
        Attack(
            title="Adjusted Horn",
            game_text="If you don't have the same number of cards in your hand as your opponent, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
