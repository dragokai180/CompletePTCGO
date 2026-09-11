from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="1c19d36e-c7e3-51ac-8a80-4fe600bbc298",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OccaBerry.Name",
    display_name="Occa Berry",
    searchable_by=["Occa Berry", "Pokémon Tool", "OccaBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=140,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Fire Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
