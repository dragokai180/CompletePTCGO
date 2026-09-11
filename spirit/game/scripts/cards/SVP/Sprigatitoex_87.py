from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d8b43f35-090d-5169-9b78-45c9dd0470a9",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatitoex.Name",
    display_name="Sprigatito ex",
    searchable_by=["Sprigatito ex", "Basic", "ex", "Sprigatitoex"],
    subtypes=["Basic", "ex"],
    collector_number=87,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=906,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Magical Leaf",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
