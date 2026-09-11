from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="46bc04e4-e842-5a02-9397-d1973252f773",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMeganiumex.Name",
    display_name="Mega Meganium ex",
    searchable_by=["Mega Meganium ex", "Stage 2", "MegaMeganiumex"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    abilities=[
        Attack(
            title="Giant Bouquet",
            game_text="This attack does 50 more damage for each [ [Grass] ] Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
