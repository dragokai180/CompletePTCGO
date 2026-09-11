from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='9b047b0c-08d7-59a2-9c03-dcf509f6f918',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name',
    display_name='Aether Paradise Conservation Area',
    searchable_by=['Aether Paradise Conservation Area', 'Stadium', 'AetherParadiseConservationArea'],
    subtypes=['Stadium'],
    collector_number=116,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Basic Grass and Basic Lightning Pokémon (both yours and your opponent's) take 30 less damage from the opponent's attacks (after applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Basic Grass and Basic Lightning Pokémon (both yours and your opponent's) take 30 less damage from the opponent's attacks (after applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
