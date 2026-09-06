from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_energy, mill_attack

_ENERGY_ON_SELF = count_energy("self")


def _has_extra_energy(ctx) -> bool:
    total_cost = sum(ctx.ability.cost.values())
    return _ENERGY_ON_SELF(ctx) >= total_cost + 2


card = PokemonCardDef(
    guid="cc239c74-6bfa-5ffc-a487-e4c93bbd4381",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaExcadrillex.Name",
    display_name="Mega Excadrill ex",
    searchable_by=["Mega Excadrill ex","Stage 1","ex","SV_Mega","MegaExcadrillex"],
    subtypes=["Stage 1","ex","SV_Mega"],
    collector_number=65,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Undermine",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.METAL: 2},
            damage=90,
            effect=mill_attack(2),
        ),
        Attack(
            title="Maximum Drilling",
            game_text="If this Pokémon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 130 more damage.",
            cost={PokemonTypes.METAL: 3},
            damage=200,
            damage_operator="+",
            effect=bonus_if(_has_extra_energy, 130),
        ),
    ],
)
