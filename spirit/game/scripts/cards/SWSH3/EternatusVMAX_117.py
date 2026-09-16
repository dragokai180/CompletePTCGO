from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play
from spirit.game.models.board import PokemonEntity
from spirit.game.session.passives import Passive, effective_pokemon_types


def _is_darkness_in_play(pokemon) -> bool:
    """Use the current field type, including Chromashift and Ability locks."""
    if not isinstance(pokemon, PokemonEntity) or pokemon.parent is None:
        return False
    if pokemon.parent.get_attribute(AttrID.NAME) not in ("bench", "activePokemonArea"):
        return False
    root = pokemon
    while root.parent is not None:
        root = root.parent
    board = getattr(root, "_board_state", None)
    return board is not None and PokemonTypes.DARKNESS.value in effective_pokemon_types(
        board, pokemon
    )


def _all_darkness_in_play(carrier) -> bool:
    player_entity = carrier.parent.parent if carrier.parent else None
    if player_entity is None:
        return False
    mons = [
        c for area in player_entity.children
        if area.get_attribute(AttrID.NAME) in ("bench", "activePokemonArea")
        for c in area.children if isinstance(c, PokemonEntity)
    ]
    return bool(mons) and all(_is_darkness_in_play(m) for m in mons)


class EternalZonePassive(Passive):
    """While every one of the owner's in-play Pokemon is Darkness type, Bench
    capacity is 8 and the owner cannot put non-Darkness Pokemon into play."""

    def blocks_pokemon_entry(self, card, player_id, carrier):
        return (
            player_id == carrier.owning_player_id
            and isinstance(card, PokemonEntity)
            and PokemonTypes.DARKNESS.value not in (
                card.get_attribute(AttrID.POKEMON_TYPES) or []
            )
            and _all_darkness_in_play(carrier)
        )

    def bench_capacity(self, player_id, carrier):
        if player_id != carrier.owning_player_id:
            return None
        return 8 if _all_darkness_in_play(carrier) else None


card = PokemonCardDef(
    guid="555f9284-d28c-56a0-b3f9-915d78cfbcb6",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusVMAX.Name",
    display_name="Eternatus VMAX",
    searchable_by=["Eternatus VMAX", "VMAX", "EternatusVMAX"],
    subtypes=["VMAX"],
    collector_number=117,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=340,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusV.Name",
    family_id=890,
    abilities=[
        Ability(
            title="Eternal Zone",
            game_text="If all of your Pok\u00e9mon in play are Darkness type, you can have up to 8 Pok\u00e9mon on your Bench, and you can't put non-Darkness Pok\u00e9mon into play. (If this Ability stops working, discard Pok\u00e9mon from your Bench until you have 5.)",
            passive=EternalZonePassive(),
        ),
        Attack(
            title="Dread End",
            game_text="This attack does 30 damage for each of your Darkness Pok\u00e9mon in play.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _is_darkness_in_play), 30),
        ),
    ],
)
