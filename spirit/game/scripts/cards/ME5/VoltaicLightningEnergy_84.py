from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class VoltaicLightningPassive(Passive):
    """The Lightning Pokémon this is attached to deals +20 to the opponent's
    Active (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.LIGHTNING.value in types:
            calc.amount += 20


card = EnergyCardDef(
    guid="4d906f0c-fb41-5857-b0c9-07d6e2dc3e71",
    key="ME5",
    name="Voltaic Lightning Energy",
    display_name="Voltaic Lightning Energy",
    searchable_by=["Voltaic Lightning Energy","Special","VoltaicLightningEnergy"],
    subtypes=["Special"],
    collector_number=84,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=True,
    passive=VoltaicLightningPassive(),
)
