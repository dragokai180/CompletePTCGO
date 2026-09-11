from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ad30ccbc-8d0c-5dbd-bc66-71031b319d70",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic", "PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Charge",
            game_text="This attack does 40 damage for each of your Pokémon that has \"Tauros\" in its name that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
