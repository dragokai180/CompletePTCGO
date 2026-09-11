from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="bf58a012-a6aa-5f66-8787-249ef119c3aa",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HabanBerry.Name",
    display_name="Haban Berry",
    searchable_by=["Haban Berry", "Pokémon Tool", "HabanBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=111,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Dragon Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
