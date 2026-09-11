from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="e22bce31-6c39-5d34-8c79-32d1d91c5a47",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AngeFloette.Name",
    display_name="Ange Floette",
    searchable_by=["Ange Floette", "Stadium", "AngeFloette"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=standard_passive("You can put this card into play only if you discard a Prism Tower in play, and you can put this card into play during the same turn you play Prism Tower.\nEach Mega Floette ex in play (both yours and your opponent's) gets +150 HP."),
    ability=standard_stadium_ability("You can put this card into play only if you discard a Prism Tower in play, and you can put this card into play during the same turn you play Prism Tower.\nEach Mega Floette ex in play (both yours and your opponent's) gets +150 HP."),
)
