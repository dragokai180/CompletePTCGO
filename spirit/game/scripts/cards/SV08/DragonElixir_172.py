from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="50d65389-5855-5217-aac8-4262900c4aeb",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonElixir.Name",
    display_name="Dragon Elixir",
    searchable_by=["Dragon Elixir", "Item", "DragonElixir"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Heal 60 damage from your Active Dragon Pokémon."),
)
