from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="8e96902d-7a32-5f45-be73-76988ff9a711",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tyme.Name",
    display_name="Tyme",
    searchable_by=["Tyme", "Supporter", "Tyme"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Tell your opponent the name of a Pokémon in your hand and put that Pokémon face down in front of you. Your opponent guesses that Pokémon's HP, and then you reveal it. If your opponent guessed right, they draw 4 cards. If they guessed wrong, you draw 4 cards. Then, return the Pokémon to your hand."),
)
