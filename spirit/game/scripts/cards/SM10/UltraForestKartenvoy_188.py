from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='fe8c8dc0-70d8-5b82-a12b-981517ad54e0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.UltraForestKartenvoy.Name',
    display_name='Ultra Forest Kartenvoy',
    searchable_by=['Ultra Forest Kartenvoy', 'Supporter', 'UltraForestKartenvoy'],
    subtypes=['Supporter'],
    collector_number=188,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("During this turn, damage from your Ultra Beasts' attacks isn't affected by any effects on your opponent's Active Pokémon."),
    condition=standard_trainer_condition("During this turn, damage from your Ultra Beasts' attacks isn't affected by any effects on your opponent's Active Pokémon."),
)
