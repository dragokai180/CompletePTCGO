from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='dfe1a87f-2507-5d8a-a85b-5e03f17d3f63',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name',
    display_name='Molayne',
    searchable_by=['Molayne', 'Supporter', 'Molayne'],
    subtypes=['Supporter'],
    collector_number=181,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you discard 2 Metal Energy cards from your hand. Shuffle a Trainer card from your discard pile into your deck.'),
    condition=standard_trainer_condition('You can play this card only if you discard 2 Metal Energy cards from your hand. Shuffle a Trainer card from your discard pile into your deck.'),
)
