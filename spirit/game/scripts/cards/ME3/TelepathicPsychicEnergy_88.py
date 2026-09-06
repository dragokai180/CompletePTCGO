from spirit.game.card_effects.energies import telepathic_psychic_on_attach
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4d6e165a-c032-556b-ad21-615e38576ac5",
    key="ME3",
    name="Telepathic Psychic Energy",
    display_name="Telepathic Psychic Energy",
    searchable_by=["Telepathic Psychic Energy", "Special", "TelepathicPsychicEnergy"],
    subtypes=["Special"],
    collector_number=88,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=True,
    on_attach=telepathic_psychic_on_attach,
)
