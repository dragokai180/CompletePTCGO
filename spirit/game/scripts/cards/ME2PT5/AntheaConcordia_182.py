from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="65d89447-d8f7-51a7-adaf-0999518118d6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntheaConcordia.Name",
    display_name="Anthea & Concordia",
    searchable_by=["Anthea & Concordia", "Supporter", "AntheaConcordia"],
    subtypes=["Supporter"],
    collector_number=182,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you have N's Darmanitan, N's Zoroark ex, N's Vanilluxe, N's Klinklang, N's Reshiram, and N's Zekrom in play.  During this turn, if your opponent's Active Pokémon is Knocked Out by damage from an attack used by your N's Pokémon, take 3 more Prize cards."),
)
