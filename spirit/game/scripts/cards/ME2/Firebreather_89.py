from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_fire_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value)


card = SupporterCardDef(
    guid="60a6fc1b-cc14-5a61-956c-aa1044535416",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Firebreather.Name",
    display_name="Firebreather",
    searchable_by=["Firebreather","Supporter","Firebreather"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_basic_fire_energy, count=7, minimum=0, reveal=True,
        prompt="Choose up to 7 Basic Fire Energy cards to put into your hand.",
    ),
)
