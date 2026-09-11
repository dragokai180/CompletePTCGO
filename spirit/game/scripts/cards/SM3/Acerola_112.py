from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='479eac05-4692-569c-aaff-d8f88dcf0b33',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name',
    display_name='Acerola',
    searchable_by=['Acerola', 'Supporter', 'Acerola'],
    subtypes=['Supporter'],
    collector_number=112,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 1 of your Pokémon that has any damage counters on it and all cards attached to it into your hand.'),
    condition=standard_trainer_condition('Put 1 of your Pokémon that has any damage counters on it and all cards attached to it into your hand.'),
)
