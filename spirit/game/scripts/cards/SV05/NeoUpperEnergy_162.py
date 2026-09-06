from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon

ALL_TYPES_TWO_AT_A_TIME = [
    [option[0].value, option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME
]


class NeoUpperPassive(Passive):
    """On a Stage 2 Pokémon: every type of Energy, 2 at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if carrier_pokemon(energy) is not holder or holder is None:
            return options
        if holder.get_attribute(AttrID.STAGE) != PokemonStage.STAGE2.value:
            return options
        return [list(opt) for opt in ALL_TYPES_TWO_AT_A_TIME]


card = EnergyCardDef(
    guid="3934254a-8d73-54fb-824f-aaafd198ed47",
    key="SV05",
    name="Neo Upper Energy",
    display_name="Neo Upper Energy",
    searchable_by=["Neo Upper Energy", "Special", "ACE SPEC"],
    subtypes=["Special", "ACE SPEC"],
    collector_number=162,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=NeoUpperPassive(),
)
