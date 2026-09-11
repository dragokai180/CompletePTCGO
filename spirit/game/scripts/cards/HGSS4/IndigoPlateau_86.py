from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='3b2b9d93-19af-5bdc-8b24-cc3e9a9fcff4',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.IndigoPlateau.Name',
    display_name='Indigo Plateau',
    searchable_by=['Indigo Plateau', 'Stadium', 'IndigoPlateau'],
    subtypes=['Stadium'],
    collector_number=86,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Each Pokémon LEGEND in play (both yours and your opponent's) gets +30 HP."),
    ability=standard_stadium_ability("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Each Pokémon LEGEND in play (both yours and your opponent's) gets +30 HP."),
)
