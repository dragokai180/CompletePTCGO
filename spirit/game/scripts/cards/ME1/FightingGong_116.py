from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand


def _fighting_energy_or_basic(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.FIGHTING.value not in types:
        return False
    return is_basic_energy_card(card) or is_basic_pokemon(card)


card = ItemCardDef(
    guid="f6c27ae9-1426-5952-86ee-7410cd49e2ba",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingGong.Name",
    display_name="Fighting Gong",
    searchable_by=["Fighting Gong","Item","FightingGong"],
    subtypes=["Item"],
    collector_number=116,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _fighting_energy_or_basic, count=1, minimum=0, reveal=True,
        prompt="Choose a Basic Fighting Energy or a Basic Fighting Pokémon.",
    ),
)
