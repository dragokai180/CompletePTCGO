from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="40d9de44-2927-5a19-abdf-d162da1db4d8",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailordex.Name",
    display_name="Wailord ex",
    searchable_by=["Wailord ex", "Stage 1", "ex", "Wailordex"],
    subtypes=["Stage 1", "ex"],
    collector_number=16,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=380,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3},
            damage=120,
        ),
        Attack(
            title="Falling Down",
            game_text="This Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 5},
            damage=270,
            effect=standard_attack,
        ),
    ],
)
