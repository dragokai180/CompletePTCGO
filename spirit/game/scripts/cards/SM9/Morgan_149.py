from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='a7ad922d-1bd6-5fcd-b378-830c4699c2af',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name',
    display_name='Morgan',
    searchable_by=['Morgan', 'Supporter', 'Morgan'],
    subtypes=['Supporter'],
    collector_number=149,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you discard Dana, Evelyn, and Nita from your hand. Look at the top 12 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('You can play this card only if you discard Dana, Evelyn, and Nita from your hand. Look at the top 12 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.'),
)
