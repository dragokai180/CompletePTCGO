from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="5fc1a94e-0f9e-5c77-889f-58a35c513c8b",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokVitalA.Name",
    display_name="Poké Vital A",
    searchable_by=["Poké Vital A", "Item", "ACE SPEC", "PokVitalA"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=62,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("You can't have more than 1 ACE SPEC card in your deck. Heal 150 damage from 1 of your Pokémon.    This card can't be put into your hand or deck from the discard pile."),
)
