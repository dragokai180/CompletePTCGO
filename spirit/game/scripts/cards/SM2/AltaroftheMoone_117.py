from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='b1d91432-5568-55f2-bd79-723bd0422afe',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheMoone.Name',
    display_name='Altar of the Moone',
    searchable_by=['Altar of the Moone', 'Stadium', 'AltaroftheMoone'],
    subtypes=['Stadium'],
    collector_number=117,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of each Pokémon (both yours and your opponent's) that has any Psychic or Darkness Energy attached to it is ColorlessColorless less. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The Retreat Cost of each Pokémon (both yours and your opponent's) that has any Psychic or Darkness Energy attached to it is ColorlessColorless less. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
