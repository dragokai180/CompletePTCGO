from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='248946ab-8c44-5aca-8a19-e37a50505a08',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MallowLana.Name',
    display_name='Mallow & Lana',
    searchable_by=['Mallow & Lana', 'Supporter', 'TAG TEAM', 'MallowLana'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=198,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Switch your Active Pokémon with 1 of your Benched Pokémon. When you play this card, you may discard 2 other cards from your hand. If you do, heal 120 damage from the Pokémon you moved to your Bench.'),
    condition=standard_trainer_condition('Switch your Active Pokémon with 1 of your Benched Pokémon. When you play this card, you may discard 2 other cards from your hand. If you do, heal 120 damage from the Pokémon you moved to your Bench.'),
)
