from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="760e883a-b915-5d40-b6d4-5782fae40b16",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsBotherBot.Name",
    display_name="Team Rocket's Bother-Bot",
    searchable_by=["Team Rocket's Bother-Bot", "Item", "TeamRocketsBotherBot"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Turn 1 of your opponent's face-down Prize cards face up and choose a random card from your opponent's hand. Your opponent reveals that card. You may have your opponent switch those cards. (That Prize card remains face up for the rest of the game.)"),
)
