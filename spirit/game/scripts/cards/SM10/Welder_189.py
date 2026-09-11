from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='94ab2c0e-e254-5d26-90ae-ad25737d73bd',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name',
    display_name='Welder',
    searchable_by=['Welder', 'Supporter', 'Welder'],
    subtypes=['Supporter'],
    collector_number=189,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach up to 2 Fire Energy cards from your hand to 1 of your Pokémon. If you do, draw 3 cards.'),
    condition=standard_trainer_condition('Attach up to 2 Fire Energy cards from your hand to 1 of your Pokémon. If you do, draw 3 cards.'),
)
