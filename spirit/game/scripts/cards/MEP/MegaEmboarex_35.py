from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e4817f65-8854-54a1-98e2-1b851d7cbb65",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEmboarex.Name",
    display_name="Mega Emboar ex",
    searchable_by=["Mega Emboar ex", "Stage 2", "MegaEmboarex", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=35,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=380,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    abilities=[
        Attack(
            title="Crimson Blast",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=320,
            effect=standard_attack,
        ),
    ],
)
