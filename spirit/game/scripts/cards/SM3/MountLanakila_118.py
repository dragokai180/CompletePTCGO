from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='80e89095-915b-574b-bdd4-5bc875641b9f',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MountLanakila.Name',
    display_name='Mount Lanakila',
    searchable_by=['Mount Lanakila', 'Stadium', 'MountLanakila'],
    subtypes=['Stadium'],
    collector_number=118,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of each Basic Pokémon in play (both yours and your opponent's) is Colorless more. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The Retreat Cost of each Basic Pokémon in play (both yours and your opponent's) is Colorless more. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
