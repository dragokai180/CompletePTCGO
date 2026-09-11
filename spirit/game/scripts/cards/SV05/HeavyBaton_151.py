from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="fd4607ce-096d-5688-85b9-c8ffeae83472",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBaton.Name",
    display_name="Heavy Baton",
    searchable_by=["Heavy Baton", "Pokémon Tool", "HeavyBaton"],
    subtypes=["Pokémon Tool"],
    collector_number=151,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to has a Retreat Cost of exactly 4, is in the Active Spot, and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 3 Basic Energy cards from that Pokémon to your Benched Pokémon in any way you like."),
)
