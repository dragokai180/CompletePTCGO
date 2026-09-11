from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='eed448cd-793c-57e1-9f9c-7409c6b27e7d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AetherFoundationEmployee.Name',
    display_name='Aether Foundation Employee',
    searchable_by=['Aether Foundation Employee', 'Supporter', 'AetherFoundationEmployee'],
    subtypes=['Supporter'],
    collector_number=168,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 3 Pokémon that have "Alolan" in their names from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put 3 Pokémon that have "Alolan" in their names from your discard pile into your hand.'),
)
