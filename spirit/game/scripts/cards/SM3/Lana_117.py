from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='08d08d68-ebe6-54a0-b651-9978fd2adb7d',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name',
    display_name='Lana',
    searchable_by=['Lana', 'Supporter', 'Lana'],
    subtypes=['Supporter'],
    collector_number=117,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 50 damage from each of your Pokémon that has any Water Energy attached to it.'),
    condition=standard_trainer_condition('Heal 50 damage from each of your Pokémon that has any Water Energy attached to it.'),
)
