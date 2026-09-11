from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='9148c756-7b30-5ce2-ba36-3ffac496e77e',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name',
    display_name='Magnetic Storm',
    searchable_by=['Magnetic Storm', 'Stadium', 'MagneticStorm'],
    subtypes=['Stadium'],
    collector_number=91,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Pokémon in play has no Resistance. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Pokémon in play has no Resistance. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
