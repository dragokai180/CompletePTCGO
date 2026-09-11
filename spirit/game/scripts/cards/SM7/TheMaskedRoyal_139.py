from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='82d93bf4-a25f-5210-94ce-bccc27c2168e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TheMaskedRoyal.Name',
    display_name='The Masked Royal',
    searchable_by=['The Masked Royal', 'Supporter', 'TheMaskedRoyal'],
    subtypes=['Supporter'],
    collector_number=139,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach a basic Energy card from your hand to one of your Stage 2 Grass, Fire, or Water Pokémon.'),
    condition=standard_trainer_condition('Attach a basic Energy card from your hand to one of your Stage 2 Grass, Fire, or Water Pokémon.'),
)
