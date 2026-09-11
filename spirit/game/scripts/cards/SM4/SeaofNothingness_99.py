from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='04a257d7-809b-512d-abb0-4e7d40f3d244',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SeaofNothingness.Name',
    display_name='Sea of Nothingness',
    searchable_by=['Sea of Nothingness', 'Stadium', 'SeaofNothingness'],
    subtypes=['Stadium'],
    collector_number=99,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Special Conditions are not removed when Pokémon (both yours and your opponent's) evolve or devolve. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Special Conditions are not removed when Pokémon (both yours and your opponent's) evolve or devolve. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
