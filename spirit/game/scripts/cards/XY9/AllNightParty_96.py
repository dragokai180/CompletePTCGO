from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='06cda8ff-46cf-5b60-8302-9eab2e539f61',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AllNightParty.Name',
    display_name='All-Night Party',
    searchable_by=['All-Night Party', 'Stadium', 'AllNightParty'],
    subtypes=['Stadium'],
    collector_number=96,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, if that player's Active Pokémon is Asleep, he or she may remove that Special Condition and heal 30 damage from that Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, if that player's Active Pokémon is Asleep, he or she may remove that Special Condition and heal 30 damage from that Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
