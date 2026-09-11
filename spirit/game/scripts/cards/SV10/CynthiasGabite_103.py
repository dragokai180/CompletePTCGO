from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a575b576-7d30-5fc3-ac88-36847c97223e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    display_name="Cynthia's Gabite",
    searchable_by=["Cynthia's Gabite", "Stage 1", "CynthiasGabite"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGible.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Champion's Call",
            game_text="Once during your turn, you may search your deck for a Cynthia's Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)
