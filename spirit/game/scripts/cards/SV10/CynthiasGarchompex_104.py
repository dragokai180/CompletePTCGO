from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ba72b81f-fc8b-5090-a644-f15150b2c1bf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGarchompex.Name",
    display_name="Cynthia's Garchomp ex",
    searchable_by=["Cynthia's Garchomp ex", "Stage 2", "ex", "CynthiasGarchompex"],
    subtypes=["Stage 2", "ex"],
    collector_number=104,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    family_id=443,
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
