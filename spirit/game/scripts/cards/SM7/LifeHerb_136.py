from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5ade656e-cffc-5c88-8aa0-0db74ad4c167',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name',
    display_name='Life Herb',
    searchable_by=['Life Herb', 'Item', 'LifeHerb'],
    subtypes=['Item'],
    collector_number=136,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, heal 60 damage and remove all Special Conditions from 1 of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip a coin. If heads, heal 60 damage and remove all Special Conditions from 1 of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
