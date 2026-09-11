from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='5514f80a-20a0-578b-97d2-aff6b78b15c6',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name',
    display_name='Martial Arts Dojo',
    searchable_by=['Martial Arts Dojo', 'Stadium', 'MartialArtsDojo'],
    subtypes=['Stadium'],
    collector_number=179,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of non-Ultra Beast Pokémon that have any basic Fighting Energy attached to them (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). If the attacking player has more Prize cards remaining than their opponent, those attacks do 40 more damage instead. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The attacks of non-Ultra Beast Pokémon that have any basic Fighting Energy attached to them (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). If the attacking player has more Prize cards remaining than their opponent, those attacks do 40 more damage instead. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
