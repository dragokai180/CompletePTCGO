from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='973254e4-58c2-502b-96d2-2ce49008a4bb',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Revitalizer.Name',
    display_name='Revitalizer',
    searchable_by=['Revitalizer', 'Item', 'Revitalizer'],
    subtypes=['Item'],
    collector_number=70,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 2 Grass Pokémon from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put 2 Grass Pokémon from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
