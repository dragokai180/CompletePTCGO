from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="7f16b916-716f-52fd-88ea-c2de5f0d14eb",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaVenusaurex.Name",
    display_name="Mega Venusaur ex",
    searchable_by=["Mega Venusaur ex", "Stage 2", "MegaVenusaurex"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=380,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    abilities=[
        Ability(
            title="Solar Transfer",
            game_text="As often as you like during your turn, you may use this Ability. Move a Basic [ [Grass] ] Energy from 1 of your Pokémon to another of your Pokémon.",
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Jungle Dump",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 4},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
