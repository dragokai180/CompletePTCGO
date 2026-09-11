from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="46c5d73b-757c-5389-9d1a-761786fbf469",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=484,
    abilities=[
        Attack(
            title="Space Crash",
            game_text="This attack does 40 damage for each Basic Energy attached to this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
