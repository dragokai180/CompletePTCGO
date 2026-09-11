from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='621b05a3-ec94-5aaf-ba07-099dfe7b2b54',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyRescue.Name',
    display_name='Buddy-Buddy Rescue',
    searchable_by=['Buddy-Buddy Rescue', 'Item', 'BuddyBuddyRescue'],
    subtypes=['Item'],
    collector_number=135,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Each player puts a Pokémon from his or her discard pile into his or her hand. (Your opponent chooses first.) You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Each player puts a Pokémon from his or her discard pile into his or her hand. (Your opponent chooses first.) You may play as many Item cards as you like during your turn (before your attack).'),
)
