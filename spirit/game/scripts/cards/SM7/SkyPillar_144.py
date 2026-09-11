from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='6b6b2fa4-989e-5220-9ea1-5610e33a303e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SkyPillar.Name',
    display_name='Sky Pillar',
    searchable_by=['Sky Pillar', 'Stadium', 'SkyPillar'],
    subtypes=['Stadium'],
    collector_number=144,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all effects of the opponent's attacks, including damage, done to Benched Pokémon (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Prevent all effects of the opponent's attacks, including damage, done to Benched Pokémon (both yours and your opponent's). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
