from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="9f55be13-4a52-5bc0-a353-a12a6929ec34",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MortysConviction.Name",
    display_name="Morty's Conviction",
    searchable_by=["Morty's Conviction", "Supporter", "MortysConviction"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you discard another card from your hand.  Draw a card for each of your opponent's Benched Pokémon."),
)
