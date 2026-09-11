from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='60d0a3af-5b9c-5c67-8aba-bff059e62847',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name',
    display_name='Bonnie',
    searchable_by=['Bonnie', 'Supporter', 'Bonnie'],
    subtypes=['Supporter'],
    collector_number=103,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if there is any Stadium card in play. Discard that Stadium card. During this turn, your Zygarde-GX can use its GX attack even if you have used your GX attack.'),
    condition=standard_trainer_condition('You can play this card only if there is any Stadium card in play. Discard that Stadium card. During this turn, your Zygarde-GX can use its GX attack even if you have used your GX attack.'),
)
