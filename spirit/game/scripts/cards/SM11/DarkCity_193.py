from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='514ebc7f-bc7d-5240-ae25-3bfb27344360',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DarkCity.Name',
    display_name='Dark City',
    searchable_by=['Dark City', 'Stadium', 'DarkCity'],
    subtypes=['Stadium'],
    collector_number=193,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Basic Darkness Pokémon in play (both yours and your opponent's) have no Retreat Cost. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Basic Darkness Pokémon in play (both yours and your opponent's) have no Retreat Cost. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
