from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="44b6fdae-1537-5af2-a8d8-c9843d30aeb2",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGreninjaex.Name",
    display_name="Mega Greninja ex",
    searchable_by=["Mega Greninja ex", "Stage 2", "MegaGreninjaex", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=81,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    abilities=[
        Ability(
            title="Mortal Shuriken",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may discard a Basic [ [Water] ] Energy card from your hand in order to use this Ability. Place 6 damage counters on 1 of your opponent's Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Ninja Spinner",
            game_text="You may put a [ [Water] ] Energy attached to this Pokémon into your hand and have this attack do 80 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
