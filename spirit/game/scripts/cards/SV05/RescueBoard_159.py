from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="eae6b14f-10f1-514c-8d68-c52845b1dc83",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueBoard.Name",
    display_name="Rescue Board",
    searchable_by=["Rescue Board", "Pokémon Tool", "RescueBoard"],
    subtypes=["Pokémon Tool"],
    collector_number=159,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of the Pokémon this card is attached to is Colorless less. If that Pokémon's remaining HP is 30 or less, it has no Retreat Cost."),
)
