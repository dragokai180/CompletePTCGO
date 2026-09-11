from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="35ca3583-e883-599d-83d8-da88c1096284",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipiti.Name",
    display_name="Fezandipiti",
    searchable_by=["Fezandipiti", "Basic", "Fezandipiti"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=1016,
    abilities=[
        Ability(
            title="Adrena-Pheromone",
            game_text="If this Pokémon has any Darkness Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            passive=standard_passive("If this Pokémon has any Darkness Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage."),
        ),
        Attack(
            title="Energy Feather",
            game_text="This attack does 30 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
