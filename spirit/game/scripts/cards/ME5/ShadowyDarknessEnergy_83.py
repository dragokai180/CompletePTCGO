from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


class ShadowyDarknessPassive(Passive):
    """The Darkness Pokémon this is attached to, while on the Bench, takes
    no damage from opposing attacks."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.target:
            return False
        if is_in_active_spot(holder):
            return False
        types = holder.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.DARKNESS.value not in types:
            return False
        return bool(calc.is_attack and calc.is_opposing)


card = EnergyCardDef(
    guid="d028a5c3-c094-5925-9374-85e7e25a44f3",
    key="ME5",
    name="Shadowy Darkness Energy",
    display_name="Shadowy Darkness Energy",
    searchable_by=["Shadowy Darkness Energy","Special","ShadowyDarknessEnergy"],
    subtypes=["Special"],
    collector_number=83,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    passive=ShadowyDarknessPassive(),
)
