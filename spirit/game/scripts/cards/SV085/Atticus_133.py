from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="5cdc599f-bcff-5ef8-aae7-6df9f1ea70a4",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Atticus.Name",
    display_name="Atticus",
    searchable_by=["Atticus", "Supporter", "Atticus"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=standard_trainer_effect("You can use this card only if your opponent's Active Pokémon is Poisoned.  Shuffle your hand into your deck. Then, draw 7 cards."),
)
