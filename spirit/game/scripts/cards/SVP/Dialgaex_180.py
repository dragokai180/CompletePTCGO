from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3d4eca34-6a75-5a7d-a4e8-5ea780258b46",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialgaex.Name",
    display_name="Dialga ex",
    searchable_by=["Dialga ex", "Basic", "ex", "Dialgaex"],
    subtypes=["Basic", "ex"],
    collector_number=180,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=483,
    abilities=[
        Attack(
            title="Time Bellow",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Metal Blast",
            game_text="This attack does 20 more damage for each Metal Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
