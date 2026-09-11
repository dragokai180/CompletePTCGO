from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5e66da37-23c4-5893-b7ea-eaef470a75b3',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BlackBelt.Name',
    display_name='Black Belt',
    searchable_by=['Black Belt', 'Supporter', 'BlackBelt'],
    subtypes=['Supporter'],
    collector_number=85,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. You may use this card only if you have more Prize cards left than your opponent. During this turn, each of your Active Pokémon's attacks does 40 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
    condition=standard_trainer_condition("You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. You may use this card only if you have more Prize cards left than your opponent. During this turn, each of your Active Pokémon's attacks does 40 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
