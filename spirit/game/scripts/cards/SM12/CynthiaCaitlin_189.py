from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e9c83471-65c5-5038-b053-46426391fc43',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name',
    display_name='Cynthia & Caitlin',
    searchable_by=['Cynthia & Caitlin', 'Supporter', 'TAG TEAM', 'CynthiaCaitlin'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=189,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put a Supporter card from your discard pile into your hand. You can't choose Cynthia & Caitlin or a card you discarded with the effect of this card. When you play this card, you may discard another card from your hand. If you do, draw 3 cards."),
    condition=standard_trainer_condition("Put a Supporter card from your discard pile into your hand. You can't choose Cynthia & Caitlin or a card you discarded with the effect of this card. When you play this card, you may discard another card from your hand. If you do, draw 3 cards."),
)
