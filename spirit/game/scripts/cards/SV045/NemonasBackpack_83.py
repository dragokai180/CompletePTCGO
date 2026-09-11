from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e652c778-7b17-5dd2-8619-a14ea11f5bf1',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.trainer.NemonasBackpack.Name',
    display_name="Nemona's Backpack",
    searchable_by=["Nemona's Backpack", 'Item', 'NemonasBackpack'],
    subtypes=['Item'],
    collector_number=83,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put up to 2 Nemona cards from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put up to 2 Nemona cards from your discard pile into your hand.'),
)
