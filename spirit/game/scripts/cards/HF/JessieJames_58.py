from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1a8dee58-25d1-594a-89ba-717784555890',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.trainer.JessieJames.Name',
    display_name='Jessie & James',
    searchable_by=['Jessie & James', 'Supporter', 'JessieJames'],
    subtypes=['Supporter'],
    collector_number=58,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('Each player discards 2 cards from their hand. Your opponent discards first.'),
    condition=standard_trainer_condition('Each player discards 2 cards from their hand. Your opponent discards first.'),
)
