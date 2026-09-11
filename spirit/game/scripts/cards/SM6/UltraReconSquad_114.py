from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4e341391-03da-5511-be85-f4b6f4381eb5',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name',
    display_name='Ultra Recon Squad',
    searchable_by=['Ultra Recon Squad', 'Supporter', 'UltraReconSquad'],
    subtypes=['Supporter'],
    collector_number=114,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard up to 2 Ultra Beast cards from your hand. Draw 3 cards for each card you discarded in this way.'),
    condition=standard_trainer_condition('Discard up to 2 Ultra Beast cards from your hand. Draw 3 cards for each card you discarded in this way.'),
)
