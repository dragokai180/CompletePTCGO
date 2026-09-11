from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="79c2e1cf-fb07-549c-b91c-78244bb60438",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    abilities=[
        Ability(
            title="Wild Growth",
            game_text="Each Basic [ [Grass] ] Energy attached to all of your Pokémon provides [ [Grass] ] [ [Grass] ] Energy. The effect of Wild Growth doesn't stack.",
            passive=standard_passive("Each Basic [ [Grass] ] Energy attached to all of your Pokémon provides [ [Grass] ] [ [Grass] ] Energy. The effect of Wild Growth doesn't stack."),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
