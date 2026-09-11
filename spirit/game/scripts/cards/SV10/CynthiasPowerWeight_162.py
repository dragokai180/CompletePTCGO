from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="56e19ace-78e5-5789-a0a5-e04be86659b6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasPowerWeight.Name",
    display_name="Cynthia's Power Weight",
    searchable_by=["Cynthia's Power Weight", "Pokémon Tool", "CynthiasPowerWeight"],
    subtypes=["Pokémon Tool"],
    collector_number=162,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Cynthia's Pokémon this card is attached to gets +70 HP."),
)
