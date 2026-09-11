from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9190592b-32c7-5093-9b78-20f93d475697',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Cassius.Name',
    display_name='Cassius',
    searchable_by=['Cassius', 'Supporter', 'Cassius'],
    subtypes=['Supporter'],
    collector_number=115,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle 1 of your Pokémon and all cards attached to it into your deck.'),
    condition=standard_trainer_condition('Shuffle 1 of your Pokémon and all cards attached to it into your deck.'),
)
