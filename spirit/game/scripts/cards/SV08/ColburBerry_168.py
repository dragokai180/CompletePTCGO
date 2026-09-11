from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="17463d28-8f3f-5726-ae41-c347cc8d3d81",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColburBerry.Name",
    display_name="Colbur Berry",
    searchable_by=["Colbur Berry", "Pokémon Tool", "ColburBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=168,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Darkness Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
