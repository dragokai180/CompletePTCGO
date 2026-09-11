from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='9ff543bc-dc73-5725-ac8e-150791e49c25',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name',
    display_name='Life Herb',
    searchable_by=['Life Herb', 'Item', 'LifeHerb'],
    subtypes=['Item'],
    collector_number=79,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, choose 1 of your Pokémon, and remove all Special Conditions and 6 damage counters from that Pokémon (all if there are less than 6).'),
    condition=standard_trainer_condition('Flip a coin. If heads, choose 1 of your Pokémon, and remove all Special Conditions and 6 damage counters from that Pokémon (all if there are less than 6).'),
)
