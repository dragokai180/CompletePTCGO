from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2e7def90-2108-51e1-ac4c-9fb8218e1dd4",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=377,
    abilities=[
        Ability(
            title="Rock Armor",
            game_text="If this Pokémon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=standard_passive("If this Pokémon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title="Breaching Lariat",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
