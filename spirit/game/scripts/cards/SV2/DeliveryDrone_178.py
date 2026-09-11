from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='9836718c-e866-5345-904b-a1019a13034a',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DeliveryDrone.Name',
    display_name='Delivery Drone',
    searchable_by=['Delivery Drone', 'Item', 'DeliveryDrone'],
    subtypes=['Item'],
    collector_number=178,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip 2 coins. If both of them are heads, search your deck for a card and put it into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Flip 2 coins. If both of them are heads, search your deck for a card and put it into your hand. Then, shuffle your deck.'),
)
