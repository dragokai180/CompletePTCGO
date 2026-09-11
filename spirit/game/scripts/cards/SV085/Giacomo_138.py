from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="61477dc1-1c94-5836-b0ee-f61148a0fd9d",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giacomo.Name",
    display_name="Giacomo",
    searchable_by=["Giacomo", "Supporter", "Giacomo"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=standard_trainer_effect("Discard a Special Energy from each of your opponent's Pokémon."),
)
