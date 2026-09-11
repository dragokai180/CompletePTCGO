from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='1779582d-7441-57d7-bb84-662f9d817aba',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RuinsofAlph.Name',
    display_name='Ruins of Alph',
    searchable_by=['Ruins of Alph', 'Stadium', 'RuinsofAlph'],
    subtypes=['Stadium'],
    collector_number=76,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Each Pokémon in play has no Resistance."),
    ability=standard_stadium_ability("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Each Pokémon in play has no Resistance."),
)
