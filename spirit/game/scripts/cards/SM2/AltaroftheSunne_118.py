from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='28c092f5-d671-5e44-9cd2-70284abb38a9',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheSunne.Name',
    display_name='Altar of the Sunne',
    searchable_by=['Altar of the Sunne', 'Stadium', 'AltaroftheSunne'],
    subtypes=['Stadium'],
    collector_number=118,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Fire Pokémon and Metal Pokémon (both yours and your opponent's) have no Weakness. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Fire Pokémon and Metal Pokémon (both yours and your opponent's) have no Weakness. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
