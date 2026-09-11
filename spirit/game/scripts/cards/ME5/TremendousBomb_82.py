from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="1ce8170b-7a3d-5c88-aba0-bbe69704ec11",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TremendousBomb.Name",
    display_name="Tremendous Bomb",
    searchable_by=["Tremendous Bomb", "Pokémon Tool", "TremendousBomb"],
    subtypes=["Pokémon Tool"],
    collector_number=82,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to isn't a Mega Evolution Pokémon ex, is in the Active Spot, and takes 240 or more damage from an attack from your opponent's Mega Evolution Pokémon ex (even if this Pokémon is Knocked Out), place 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card."),
)
