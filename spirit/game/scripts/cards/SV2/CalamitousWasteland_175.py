from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='27764a23-fd06-537f-a949-8b742e06b348',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CalamitousWasteland.Name',
    display_name='Calamitous Wasteland',
    searchable_by=['Calamitous Wasteland', 'Stadium', 'CalamitousWasteland'],
    subtypes=['Stadium'],
    collector_number=175,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of each Basic non-Fighting Pokémon in play\xa0(both yours and your opponent's)\xa0is Colorless more."),
    ability=standard_stadium_ability("The Retreat Cost of each Basic non-Fighting Pokémon in play\xa0(both yours and your opponent's)\xa0is Colorless more."),
)
