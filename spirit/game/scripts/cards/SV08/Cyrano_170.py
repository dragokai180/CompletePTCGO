from spirit.game.data_utils import SupporterCardDef, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_pokemon_card


def _is_pokemon_ex(card) -> bool:
    return is_pokemon_card(card) and is_pokemon_ex(card.archetype_id)


card = SupporterCardDef(
    guid="6dac3731-b1e4-5c98-bc9f-33229a0c158e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyrano.Name",
    display_name="Cyrano",
    searchable_by=["Cyrano", "Supporter", "Cyrano"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=search_to_hand(
        predicate=_is_pokemon_ex,
        count=3,
        reveal=True,
        prompt="Choose up to 3 Pokémon ex to put into your hand.",
    ),
)
