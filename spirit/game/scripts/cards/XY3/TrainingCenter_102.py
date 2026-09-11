from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='9f716805-d6d8-5400-bd3a-d295e751aacd',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TrainingCenter.Name',
    display_name='Training Center',
    searchable_by=['Training Center', 'Stadium', 'TrainingCenter'],
    subtypes=['Stadium'],
    collector_number=102,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Stage 1 and Stage 2 Pokémon in play (both yours and your opponent's) gets +30 HP. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Stage 1 and Stage 2 Pokémon in play (both yours and your opponent's) gets +30 HP. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
