from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import ability_lock_passive


def _is_colorless_pokemon(pokemon, carrier) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.COLORLESS.value in types


card = StadiumCardDef(
    guid="ec5cbd72-6e4a-57c2-94bf-df586f1ee13a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsWatchtower.Name",
    display_name="Team Rocket's Watchtower",
    searchable_by=["Team Rocket's Watchtower", "Stadium", "TeamRocketsWatchtower"],
    subtypes=["Stadium"],
    collector_number=180,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=ability_lock_passive(_is_colorless_pokemon),
)
