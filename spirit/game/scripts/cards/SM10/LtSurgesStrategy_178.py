from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4adcd302-f528-5c6e-afe4-653e842e3ee5',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesStrategy.Name',
    display_name="Lt. Surge's Strategy",
    searchable_by=["Lt. Surge's Strategy", 'Supporter', 'LtSurgesStrategy'],
    subtypes=['Supporter'],
    collector_number=178,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you have more Prize cards remaining than your opponent. During this turn, you can play 3 Supporter cards (including this card).'),
    condition=standard_trainer_condition('You can play this card only if you have more Prize cards remaining than your opponent. During this turn, you can play 3 Supporter cards (including this card).'),
)
