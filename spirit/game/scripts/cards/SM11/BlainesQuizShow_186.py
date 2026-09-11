from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='a8f982cb-3831-5788-97f0-2abb7064c632',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuizShow.Name',
    display_name="Blaine's Quiz Show",
    searchable_by=["Blaine's Quiz Show", 'Supporter', 'BlainesQuizShow'],
    subtypes=['Supporter'],
    collector_number=186,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put a Pokémon from your hand face down in front of you and tell your opponent the name of an attack it has. Your opponent guesses the name of that Pokémon, and then you reveal it. If your opponent guessed right, they draw 4 cards. If they guessed wrong, you draw 4 cards. Return the Pokémon to your hand.'),
    condition=standard_trainer_condition('Put a Pokémon from your hand face down in front of you and tell your opponent the name of an attack it has. Your opponent guesses the name of that Pokémon, and then you reveal it. If your opponent guessed right, they draw 4 cards. If they guessed wrong, you draw 4 cards. Return the Pokémon to your hand.'),
)
