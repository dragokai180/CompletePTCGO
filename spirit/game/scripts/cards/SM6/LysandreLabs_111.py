from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='f885b1a4-7263-52f1-99a1-7d0e9e26edb8',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LysandreLabs.Name',
    display_name='Lysandre Labs',
    searchable_by=['Lysandre Labs', 'Stadium', 'LysandreLabs'],
    subtypes=['Stadium'],
    collector_number=111,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Pokémon Tool cards in play (both yours and your opponent's) have no effect. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Pokémon Tool cards in play (both yours and your opponent's) have no effect. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
