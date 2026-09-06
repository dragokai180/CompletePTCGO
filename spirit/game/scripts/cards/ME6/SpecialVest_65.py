from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.passives import carrier_pokemon


def _not_mega_ex_holder(target, carrier):
    if carrier_pokemon(carrier) is not target:
        return False
    return "SV_Mega" not in subtypes_for(target.archetype_id)


def _is_mega_ex_attacker(attacker):
    return "SV_Mega" in subtypes_for(attacker.archetype_id)


card = PokemonToolCardDef(
    guid="cdeecd9b-b671-5e8a-abca-c700a6780f5f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialVest.Name",
    display_name="Special Vest",
    searchable_by=["Special Vest","Tool","SpecialVest"],
    subtypes=["Tool"],
    collector_number=65,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(
        60, protects=_not_mega_ex_holder, attacker_pred=_is_mega_ex_attacker,
    ),
)
