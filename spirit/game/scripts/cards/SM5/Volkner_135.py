from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='03be53aa-c19f-5a03-b6cf-13c6de2496f4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name',
    display_name='Volkner',
    searchable_by=['Volkner', 'Supporter', 'Volkner'],
    subtypes=['Supporter'],
    collector_number=135,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for an Item card and a Lightning Energy card, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for an Item card and a Lightning Energy card, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
