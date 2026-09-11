from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="45f8a462-29d2-58b1-a8dc-79f1918a9c70",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Levincia.Name",
    display_name="Levincia",
    searchable_by=["Levincia", "Stadium", "Levincia"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may put up to 2 Basic Lightning Energy cards from their discard pile into their hand."),
    ability=standard_stadium_ability("Once during each player's turn, that player may put up to 2 Basic Lightning Energy cards from their discard pile into their hand."),
)
