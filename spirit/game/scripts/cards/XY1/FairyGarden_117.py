from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='3795d02e-1bd6-5a7f-8d79-c1b2548cd42d',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name',
    display_name='Fairy Garden',
    searchable_by=['Fairy Garden', 'Stadium', 'FairyGarden'],
    subtypes=['Stadium'],
    collector_number=117,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Pokémon that has any Fairy Energy attached to it (both yours and your opponent's) has no Retreat Cost. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Pokémon that has any Fairy Energy attached to it (both yours and your opponent's) has no Retreat Cost. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
