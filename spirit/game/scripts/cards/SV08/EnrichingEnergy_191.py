from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import enriching_energy_on_attach

card = EnergyCardDef(
    guid="c0b69a59-9591-516a-abb5-3d8910b0cc9f",
    key="SV08",
    name="Enriching Energy",
    display_name="Enriching Energy",
    searchable_by=["Enriching Energy","Special","ACE SPEC","EnrichingEnergy"],
    subtypes=["Special","ACE SPEC"],
    collector_number=191,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=enriching_energy_on_attach,
)
