from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="b2d1d8e8-308a-59cd-a63a-1cf37fc28c6f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdversityPolicy.Name",
    display_name="Adversity Policy",
    searchable_by=["Adversity Policy", "Pokémon Tool", "AdversityPolicy"],
    subtypes=["Pokémon Tool"],
    collector_number=74,
    set_code="ME4",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to has Weakness to your opponent's Active Pokémon's type, is in the Active Spot, and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), draw 3 cards."),
)
