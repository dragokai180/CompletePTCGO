from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="06b6d74d-7d2a-5ad4-af22-342efd1fec1a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGarchompex.Name",
    display_name="Cynthia's Garchomp ex",
    searchable_by=["Cynthia's Garchomp ex", "Stage 2", "ex", "CynthiasGarchompex"],
    subtypes=["Stage 2", "ex"],
    collector_number=204,
    set_code="SVP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    abilities=[
        Attack(
            title="Corkscrew Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title="Draconic Buster",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=260,
            effect=standard_attack,
        ),
    ],
)
