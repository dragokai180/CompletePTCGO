from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c6b34e84-ef62-5d12-867e-c9ea770e6589",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardYex.Name",
    display_name="Mega Charizard Y ex",
    searchable_by=["Mega Charizard Y ex", "Stage 2", "MegaCharizardYex"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    abilities=[
        Attack(
            title="Explosion Y",
            game_text="Discard 3 Energy from this Pokémon, and this attack does 280 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
