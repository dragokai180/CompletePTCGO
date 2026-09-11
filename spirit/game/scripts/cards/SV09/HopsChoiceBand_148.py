from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="506f6862-b24c-55b5-9a3e-59ec4f5ff738",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsChoiceBand.Name",
    display_name="Hop's Choice Band",
    searchable_by=["Hop's Choice Band", "Pokémon Tool", "HopsChoiceBand"],
    subtypes=["Pokémon Tool"],
    collector_number=148,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Attacks used by the Hop's Pokémon this card is attached to cost Colorless less and do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
