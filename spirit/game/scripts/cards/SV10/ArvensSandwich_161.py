from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="bae4ddf4-97b5-5022-a9ae-11c207d6ebe5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArvensSandwich.Name",
    display_name="Arven's Sandwich",
    searchable_by=["Arven's Sandwich", "Item", "ArvensSandwich"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Heal 30 damage from your Active Pokémon. If that Pokémon is an Arven's Pokémon, heal 100 damage from it instead."),
)
