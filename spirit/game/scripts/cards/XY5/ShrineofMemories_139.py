from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='23a9102a-c29c-510f-a38e-8d8488f7a361',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name',
    display_name='Shrine of Memories',
    searchable_by=['Shrine of Memories', 'Stadium', 'ShrineofMemories'],
    subtypes=['Stadium'],
    collector_number=139,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each player's evolved Pokémon can use any attack from its previous Evolutions. (That player still needs the necessary Energy to use each attack.) This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each player's evolved Pokémon can use any attack from its previous Evolutions. (That player still needs the necessary Energy to use each attack.) This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
