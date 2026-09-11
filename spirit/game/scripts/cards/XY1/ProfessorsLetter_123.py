from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='21203d92-01e2-5ef5-98a5-e62266cc3807',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name',
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", 'Item', 'ProfessorsLetter'],
    subtypes=['Item'],
    collector_number=123,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
)
