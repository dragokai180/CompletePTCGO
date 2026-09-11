from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='a662e600-bd33-50bd-9832-dac9d73d0729',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CalamitousSnowyMountain.Name',
    display_name='Calamitous Snowy Mountain',
    searchable_by=['Calamitous Snowy Mountain', 'Stadium', 'CalamitousSnowyMountain'],
    subtypes=['Stadium'],
    collector_number=174,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('Whenever any player attaches an Energy card from their hand to 1 of their Basic non-Water Pokémon, put 2 damage counters on that Pokémon.'),
    ability=standard_stadium_ability('Whenever any player attaches an Energy card from their hand to 1 of their Basic non-Water Pokémon, put 2 damage counters on that Pokémon.'),
)
