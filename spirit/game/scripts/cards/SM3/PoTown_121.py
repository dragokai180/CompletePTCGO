from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='47e7adfc-ca5b-5eaf-ab1e-cf478e51515d',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PoTown.Name',
    display_name='Po Town',
    searchable_by=['Po Town', 'Stadium', 'PoTown'],
    subtypes=['Stadium'],
    collector_number=121,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Whenever any player plays a Pokémon from their hand to evolve 1 of their Pokémon, put 3 damage counters on that Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Whenever any player plays a Pokémon from their hand to evolve 1 of their Pokémon, put 3 damage counters on that Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
