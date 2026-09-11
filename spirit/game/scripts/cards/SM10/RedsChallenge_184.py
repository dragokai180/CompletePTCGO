from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='878ce0c1-8979-539b-a8c1-3bbe352c0a68',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name',
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", 'Supporter', 'RedsChallenge'],
    subtypes=['Supporter'],
    collector_number=184,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('You can play this card only if you discard 2 other cards from your hand. Search your deck for a card and put it into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('You can play this card only if you discard 2 other cards from your hand. Search your deck for a card and put it into your hand. Then, shuffle your deck.'),
)
