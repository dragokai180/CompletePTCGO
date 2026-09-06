from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import (
    Rarities,
    AttrID,
    SpecialConditions,
    CLIENT_SPECIAL_CONDITION_NAMES,
)
from spirit.game.session.passives import Passive, carrier_pokemon


MochiGuid = "a08b2d92-ddc0-450d-b9e5-faaee9989638"


class _BindingMochiPassive(Passive):
    """If the holder is Poisoned, its attacks deal +40 to the opponent Active."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is None:
            return
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        conditions = holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] in conditions:
            calc.amount += 40


card = PokemonToolCardDef(
    guid=MochiGuid,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BindingMochi.Name",
    display_name="Binding Mochi",
    searchable_by=["Binding Mochi", "Pokémon Tool", "BindingMochi"],
    subtypes=["Pokémon Tool"],
    collector_number=55,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=_BindingMochiPassive(),
)

