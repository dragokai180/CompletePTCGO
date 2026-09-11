from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="6362d92e-544b-52e9-af39-75053a90bb2a",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveryCharm.Name",
    display_name="Bravery Charm",
    searchable_by=["Bravery Charm", "Pokémon Tool", "BraveryCharm"],
    subtypes=["Pokémon Tool"],
    collector_number=175,
    set_code="SV07",
    regulation_mark="G",
    rarity=Rarities.RareRainbow,
    passive=standard_passive("The Basic Pokémon this card is attached to gets +50 HP."),
)
