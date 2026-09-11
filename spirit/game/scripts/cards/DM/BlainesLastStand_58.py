from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='87ce236a-7ef6-5bef-b96f-309a975d7373',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name',
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", 'Supporter', 'BlainesLastStand'],
    subtypes=['Supporter'],
    collector_number=58,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('You can play this card only when it is the last card in your hand. Draw 2 cards for each Fire Pokémon you have in play.'),
    condition=standard_trainer_condition('You can play this card only when it is the last card in your hand. Draw 2 cards for each Fire Pokémon you have in play.'),
)
