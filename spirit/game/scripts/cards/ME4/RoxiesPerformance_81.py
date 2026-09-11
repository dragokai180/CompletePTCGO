from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="02921fc9-6079-5fe1-98ef-80e9a5bdbe6c",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoxiesPerformance.Name",
    display_name="Roxie's Performance",
    searchable_by=["Roxie's Performance", "Supporter", "RoxiesPerformance"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("During your opponent's next turn, their Poisoned Pokémon can't retreat. (This includes newly Poisoned Pokémon.)"),
)
