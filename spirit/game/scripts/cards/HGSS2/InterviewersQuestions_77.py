from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='597533d4-85b6-55bc-bda6-ed08f2894372',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.InterviewersQuestions.Name',
    display_name="Interviewer's Questions",
    searchable_by=["Interviewer's Questions", 'Supporter', 'InterviewersQuestions'],
    subtypes=['Supporter'],
    collector_number=77,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Look at the top 8 cards of your deck. Choose as many Energy cards as you like, show them to your opponent, and put them into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Look at the top 8 cards of your deck. Choose as many Energy cards as you like, show them to your opponent, and put them into your hand. Shuffle the other cards back into your deck.'),
)
