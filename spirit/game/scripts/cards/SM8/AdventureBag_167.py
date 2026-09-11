from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5767eea9-0589-5ace-b7de-4fb230fa6a06',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name',
    display_name='Adventure Bag',
    searchable_by=['Adventure Bag', 'Item', 'AdventureBag'],
    subtypes=['Item'],
    collector_number=167,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for up to 2 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
