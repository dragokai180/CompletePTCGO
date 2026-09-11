from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='179ced6b-9e34-5aad-84db-cd63f983be9b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Miriam.Name',
    display_name='Miriam',
    searchable_by=['Miriam', 'Supporter', 'Miriam'],
    subtypes=['Supporter'],
    collector_number=179,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle up to 5 Pokémon from your discard pile into your deck. If you shuffled any cards into your deck in this way, draw 3 cards.'),
    condition=standard_trainer_condition('Shuffle up to 5 Pokémon from your discard pile into your deck. If you shuffled any cards into your deck in this way, draw 3 cards.'),
)
