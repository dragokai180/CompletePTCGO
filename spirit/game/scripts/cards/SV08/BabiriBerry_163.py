from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="44960f9e-3b9b-5016-9c05-9534dfd80a1a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BabiriBerry.Name",
    display_name="Babiri Berry",
    searchable_by=["Babiri Berry", "Pokémon Tool", "BabiriBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=163,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Metal Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
