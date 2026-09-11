from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='c6fc8d01-d342-5e2a-891a-4fa09765b4c5',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RoughSeas.Name',
    display_name='Rough Seas',
    searchable_by=['Rough Seas', 'Stadium', 'RoughSeas'],
    subtypes=['Stadium'],
    collector_number=137,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may heal 30 damage from each of his or her Water Pokémon and Lightning Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may heal 30 damage from each of his or her Water Pokémon and Lightning Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
