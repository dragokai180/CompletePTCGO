from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import treasure_on_taken_as_prize

card = EnergyCardDef(
    guid="d193d412-b5e1-5751-a2ac-103c8ac26360",
    key="SWSH7",
    name="Treasure Energy",
    display_name="Treasure Energy",
    searchable_by=["Treasure Energy", "Special"],
    subtypes=["Special"],
    collector_number=165,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    abilities=[Ability(
        title="Treasure Energy",
        game_text=(
            "If you took this card as a face-down Prize card during your "
            "turn, before you put it into your hand, you may attach this "
            "card to 1 of your Pokémon."
        ),
        trigger=Triggers.ON_TAKEN_AS_PRIZE,
        effect=treasure_on_taken_as_prize,
    )],
)
