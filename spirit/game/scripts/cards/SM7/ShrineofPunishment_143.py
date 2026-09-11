from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='f3eb7eaf-99b4-5356-9f22-2039c546c38f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name',
    display_name='Shrine of Punishment',
    searchable_by=['Shrine of Punishment', 'Stadium', 'ShrineofPunishment'],
    subtypes=['Stadium'],
    collector_number=143,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Between turns, put 1 damage counter on each Pokémon-GX and Pokémon-EX (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Between turns, put 1 damage counter on each Pokémon-GX and Pokémon-EX (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
