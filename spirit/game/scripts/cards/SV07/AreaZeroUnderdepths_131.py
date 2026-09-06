from spirit.game.data_utils import StadiumCardDef, subtypes_for
from spirit.game.attributes import AttrID, Rarities
from spirit.game.models.board import PlayerEntity, PokemonEntity
from spirit.game.session.passives import Passive


def _player_has_tera(playmat, player_id) -> bool:
    player_entity = next(
        (c for c in playmat.children
         if isinstance(c, PlayerEntity) and c.owning_player_id == player_id),
        None,
    )
    if player_entity is None:
        return False
    for area in player_entity.children:
        if area.get_attribute(AttrID.NAME) not in ("bench", "activePokemonArea"):
            continue
        for child in area.children:
            if isinstance(child, PokemonEntity) \
                    and "Tera" in subtypes_for(child.archetype_id):
                return True
    return False


class AreaZeroUnderdepthsPassive(Passive):
    """Each player who has any Tera Pokémon in play can have up to 8 on Bench.
    When that stops applying, enforce_bench_capacity discards excess to 5."""

    def bench_capacity(self, player_id, carrier):
        # Stadium: carrier -> activeStadium -> playmat
        playmat = carrier.parent.parent if carrier.parent else None
        if playmat is None:
            return None
        return 8 if _player_has_tera(playmat, player_id) else None


card = StadiumCardDef(
    guid="39d97d1a-4079-5b77-a479-4d7f1a84b452",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AreaZeroUnderdepths.Name",
    display_name="Area Zero Underdepths",
    searchable_by=["Area Zero Underdepths", "Stadium", "AreaZeroUnderdepths"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=AreaZeroUnderdepthsPassive(),
)
