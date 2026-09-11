from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='247b5520-cbb1-5b07-8890-00e4bf8b64a4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name',
    display_name='Power Plant',
    searchable_by=['Power Plant', 'Stadium', 'PowerPlant'],
    subtypes=['Stadium'],
    collector_number=183,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Pokémon-GX and Pokémon-EX in play (both yours and your opponent's) have no Abilities. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Pokémon-GX and Pokémon-EX in play (both yours and your opponent's) have no Abilities. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
