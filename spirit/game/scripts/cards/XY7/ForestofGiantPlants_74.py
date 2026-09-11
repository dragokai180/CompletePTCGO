from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='aedb9e18-b3de-5561-a0ba-57491ab1a270',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ForestofGiantPlants.Name',
    display_name='Forest of Giant Plants',
    searchable_by=['Forest of Giant Plants', 'Stadium', 'ForestofGiantPlants'],
    subtypes=['Stadium'],
    collector_number=74,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each player's Grass Pokémon can evolve during his or her first turn or the turn he or she plays those Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each player's Grass Pokémon can evolve during his or her first turn or the turn he or she plays those Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
