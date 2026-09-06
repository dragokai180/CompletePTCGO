from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_basic_pokemon


def _is_basic_team_rockets(card) -> bool:
    if not is_basic_pokemon(card):
        return False
    definition = def_for(card.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


card = SupporterCardDef(
    guid="71411299-4113-5009-9616-0e30885014cf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsProton.Name",
    display_name="Team Rocket's Proton",
    searchable_by=["Team Rocket's Proton", "Supporter", "TeamRocketsProton"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    usable_first_turn=True,
    condition=deck_nonempty,
    effect=search_to_hand(
        _is_basic_team_rockets, count=3, minimum=0,
        prompt="Choose up to 3 Basic Team Rocket's Pokémon.",
    ),
)
