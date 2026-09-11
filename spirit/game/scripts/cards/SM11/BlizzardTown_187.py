from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='ffa144f0-2019-5f28-aae1-162235036ea5',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BlizzardTown.Name',
    display_name='Blizzard Town',
    searchable_by=['Blizzard Town', 'Stadium', 'BlizzardTown'],
    subtypes=['Stadium'],
    collector_number=187,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Pokémon with 40 HP or less remaining (both yours and your opponent's) can't attack. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Pokémon with 40 HP or less remaining (both yours and your opponent's) can't attack. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
