from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="cb29cdbd-6fc3-5402-b2d3-4a58351f626d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThickScale.Name",
    display_name="Thick Scale",
    searchable_by=["Thick Scale", "Pokémon Tool", "ThickScale"],
    subtypes=["Pokémon Tool"],
    collector_number=211,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Dragon Pokémon this card is attached to takes 50 less damage from attacks from your opponent's Grass, Fire, Water, or Lightning Pokémon (after applying Weakness and Resistance)."),
)
