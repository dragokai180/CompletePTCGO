from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="15f36567-294e-5228-8406-64340afd3780",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pokémon Tool", "CounterGain"],
    subtypes=["Pokémon Tool"],
    collector_number=169,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If you have more Prize cards remaining than your opponent, attacks used by the Pokémon this card is attached to cost Colorless less."),
)
