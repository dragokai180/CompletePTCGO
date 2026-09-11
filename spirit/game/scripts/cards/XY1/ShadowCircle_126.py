from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='afd45c1b-a248-5969-b353-fdc1f4061b38',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ShadowCircle.Name',
    display_name='Shadow Circle',
    searchable_by=['Shadow Circle', 'Stadium', 'ShadowCircle'],
    subtypes=['Stadium'],
    collector_number=126,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Pokémon that has any Darkness Energy attached to it (both yours and your opponent's) has no Weakness. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Pokémon that has any Darkness Energy attached to it (both yours and your opponent's) has no Weakness. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
