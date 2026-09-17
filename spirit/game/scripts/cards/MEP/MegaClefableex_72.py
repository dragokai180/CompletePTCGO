from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0c67bd66-50c4-5633-9dd2-e306b89f32b1",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaClefableex.Name",
    display_name="Mega Clefable ex",
    searchable_by=["Mega Clefable ex", "Stage 1", "MegaClefableex", "ex", "SV_Mega"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=72,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    abilities=[
        Ability(
            title="Luminous Wing",
            game_text="Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
            passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
        ),
        Attack(
            title="Shooting Moons",
            game_text="You may discard up to 4 Energy cards from your hand, and this attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
