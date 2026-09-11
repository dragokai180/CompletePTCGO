from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='04a9f03e-8f5c-5b8d-a5a2-661a1dc0ed92',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name',
    display_name='Tag Call',
    searchable_by=['Tag Call', 'Item', 'TagCall'],
    subtypes=['Item'],
    collector_number=206,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 TAG TEAM cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for up to 2 TAG TEAM cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
