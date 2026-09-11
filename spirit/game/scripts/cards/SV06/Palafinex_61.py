from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="02ef9cc7-e142-56f4-903d-a4edc4431755",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafinex.Name",
    display_name="Palafin ex",
    searchable_by=["Palafin ex", "Stage 1", "ex", "Palafinex"],
    subtypes=["Stage 1", "ex"],
    collector_number=61,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    unplayable_from_hand=True,
    abilities=[
        Ability(
            title="Hero's Spirit",
            game_text="Put this Pokémon into play only with the effect of Palafin's Zero to Hero Ability.",
            passive=standard_passive("Put this Pokémon into play only with the effect of Palafin's Zero to Hero Ability."),
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1},
            damage=250,
            effect=standard_attack,
        ),
    ],
)
