from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import bonus_if, count_energy
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive

_ENERGY_ON_SELF = count_energy("self")

_BLOCKED_TRAINER_TYPES = (
    TrainerType.ITEM.value,
    TrainerType.POKEMON_TOOL.value,
    TrainerType.POKEMON_TOOL_F.value,
)

class OceanicCursePassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) in _BLOCKED_TRAINER_TYPES


def _has_extra_energy(ctx) -> bool:
    total_cost = sum(ctx.ability.cost.values())
    return _ENERGY_ON_SELF(ctx) >= total_cost + 2


card = PokemonCardDef(
    guid="47555ed5-3147-52e2-82d4-5baf7fa4ef03",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicentex.Name",
    display_name="Jellicent ex",
    searchable_by=["Jellicent ex","Stage 1","ex","Jellicentex"],
    subtypes=["Stage 1","ex"],
    collector_number=45,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Oceanic Curse",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Item cards or Pokémon Tool cards from their hand.",
            passive=OceanicCursePassive(),
        ),
        Attack(
            title="Power Press",
            game_text="If this Pokémon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_has_extra_energy, 80),
        ),
    ],
)
