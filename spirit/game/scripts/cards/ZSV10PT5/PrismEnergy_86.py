from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class PrismEnergyPassive(Passive):
    """On a Basic Pokémon, provides every type of Energy, 1 at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if carrier_pokemon(energy) is not holder or holder is None:
            return options
        if holder.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            return options
        return [[option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME]


card = EnergyCardDef(
    guid="f7570c28-92a7-5fe1-9fdb-901004795357",
    key="ZSV10PT5",
    name="Prism Energy",
    display_name="Prism Energy",
    searchable_by=["Prism Energy","Special","PrismEnergy"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=PrismEnergyPassive(),
)
