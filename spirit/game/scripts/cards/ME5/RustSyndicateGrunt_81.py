from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="e5f466a6-562d-5ad7-914a-d8a55e5c7e4d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RustSyndicateGrunt.Name",
    display_name="Rust Syndicate Grunt",
    searchable_by=["Rust Syndicate Grunt", "Supporter", "RustSyndicateGrunt"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if any of your Pokémon were Knocked Out during your opponent's last turn.\n\nDiscard an Energy from 1 of your opponent's Pokémon."),
)
