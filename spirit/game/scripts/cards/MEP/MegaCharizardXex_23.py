from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="79dcbcb5-f649-5281-8f3a-e39b2ef031c9",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardXex.Name",
    display_name="Mega Charizard X ex",
    searchable_by=["Mega Charizard X ex", "Stage 2", "MegaCharizardXex", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=23,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    abilities=[
        Attack(
            title="Inferno X",
            game_text="Discard any amount of [ [Fire] ] Energy from among your Pokémon, and this attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
