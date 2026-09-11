from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="14be13a1-b105-5bc2-8ebf-bdd61641c480",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreads.Name",
    display_name="Iron Treads",
    searchable_by=["Iron Treads", "Basic", "Future", "IronTreads"],
    subtypes=["Basic", "Future"],
    collector_number=118,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=990,
    abilities=[
        Ability(
            title="Dual Core",
            game_text="As long as this Pokémon has a Future Booster Energy Capsule attached, it is Fighting and Metal type.",
            passive=standard_passive("As long as this Pokémon has a Future Booster Energy Capsule attached, it is Fighting and Metal type."),
        ),
        Attack(
            title="Wheel Pass",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
